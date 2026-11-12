import sys
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import rankings as r


def comment(work_id, count=0, login=r.BOT, comment_id=1):
    return {'id': comment_id, 'user': {'login': login, 'type': 'Bot' if login == r.BOT else 'User'},
            'body': r.ballot_marker(work_id), 'html_url': f'https://github.com/test/issues/1#issuecomment-{comment_id}',
            'reactions': {'+1': count, 'heart': 100}}


class RankingsTest(unittest.TestCase):
    def test_catalog_scope_and_deduplication(self):
        readme = '''## Games
| **First** | Author | Game | [Post](https://x.com/creator/status/123) | [Code](https://github.com/a/shared/tree/main/one) | X: 1,234 views, 2 likes<br>2026-11-11 11:32 UTC<br>GitHub: 0 stars, 1 fork<br>2026-11-11 12:00 UTC |
| **Second** | Author | Game | [Post](https://x.com/creator/status/123) | [Code](https://github.com/a/shared/tree/main/two) | — |
## Community feedback and discussion
| **Gameplay depth** | Person | Opinion | [Source](https://x.com/person/status/456) | — | X: 999 views<br>2026-11-11 11:32 UTC |
'''
        works, sources = r.catalog(readme, '| First | Verified / 已核实 | Evidence |')
        self.assertEqual(len(works), 2)
        self.assertNotIn('Gameplay depth', [w['name'] for w in works.values()])
        shared = sources['GitHub:a/shared']
        self.assertEqual(len(shared['works']), 2)
        self.assertEqual(shared['metrics']['stars'], 0)
        self.assertEqual(sources['X:123']['metrics']['views'], 1234)
        self.assertEqual(sources['X:123']['observed_at'], '2026-11-11T11:32:00Z')
        self.assertEqual(r.source_url('Bilibili', ['https://www.bilibili.com/video/BV1yJW168ENZ/'])[1], 'BV1yJW168ENZ')
        self.assertEqual(r.source_url('YouTube', ['https://youtu.be/WREAJZnAA2k'])[1], 'WREAJZnAA2k')

    def test_missing_is_not_zero_and_newer_cache_wins(self):
        s = {'a': {'metrics': {}, 'observed_at': None, 'status': 'unavailable'}}
        r.restore_snapshots(s, {'a': {'metrics': {'views': 0}, 'observed_at': '2026-11-12T00:00:00Z', 'status': 'ok'}})
        self.assertEqual(s['a']['metrics']['views'], 0)
        r.restore_snapshots(s, {'a': {'metrics': {'views': 99}, 'observed_at': '2026-11-11T00:00:00Z'}})
        self.assertEqual(s['a']['metrics']['views'], 0)
        self.assertEqual(r.counts({'views': None, 'likes': 0}, {'views': 'views', 'likes': 'likes'}), {'likes': 0})

    def test_refresh_failure_preserves_observation(self):
        s = {'x': {'platform': 'X', 'metrics': {'views': 9}, 'observed_at': '2026-11-11T00:00:00Z'}}
        with patch.object(r, 'fetch_metrics', side_effect=ValueError('bad API')), patch.object(r.time, 'sleep'):
            r.refresh_sources(s)
        self.assertEqual(s['x']['metrics']['views'], 9)
        self.assertEqual(s['x']['observed_at'], '2026-11-11T00:00:00Z')
        self.assertEqual(s['x']['status'], 'stale')

    def test_missing_primary_metric_preserves_observation(self):
        s = {'x': {'platform': 'X', 'metrics': {'views': 9}, 'observed_at': 'old'}}
        with patch.object(r, 'fetch_metrics', return_value={'likes': 2}), patch.object(r.time, 'sleep'):
            r.refresh_sources(s)
        self.assertEqual(s['x']['metrics'], {'views': 9})
        self.assertEqual(s['x']['status'], 'stale')

    def test_incomplete_http_response_retains_snapshot(self):
        s = {'x': {'platform': 'X', 'metrics': {'views': 9}, 'observed_at': 'old'}}
        with patch.object(r, 'fetch_metrics', side_effect=r.http.client.IncompleteRead(b'partial', 10)):
            r.refresh_sources(s)
        self.assertEqual(s['x']['metrics']['views'], 9)
        self.assertEqual(s['x']['status'], 'stale')
        self.assertEqual(s['x']['error'], 'IncompleteRead')

    def test_ties_include_zero(self):
        result = list(r.ranked([('b', 3), ('a', 3), ('d', 0), ('c', 0)], lambda i: i[1]))
        self.assertEqual([rank for rank, _ in result], [1, 1, 3, 3])
        self.assertEqual([item[0] for _, item in result], ['a', 'b', 'c', 'd'])

    def test_bot_identity_and_duplicate_protection(self):
        work_id = 'a' * 16
        self.assertEqual(r.ballot_comments([comment(work_id, login='reader')], {work_id: {}}), {})
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            r.ballot_comments([comment(work_id), comment(work_id, comment_id=2)], {work_id: {}})

    def test_comment_pagination(self):
        with patch.object(r, 'github', side_effect=[[{}] * 100, [{}] * 43]) as api:
            self.assertEqual(len(r.pages('/issues/1/comments')), 143)
            self.assertIn('page=2', api.call_args[0][0])

    def test_votes_only_count_thumbs_up_and_support_withdrawal(self):
        work_id = 'a' * 16
        registry = {'repository': r.REPOSITORY, 'issue_number': 1}
        issue = {'user': {'login': r.BOT, 'type': 'Bot'}, 'body': r.ISSUE_MARKER, 'state': 'open'}
        previous = {'observed_at': 'old', 'works': {work_id: {'votes': 4}}}
        with patch.object(r, 'github', return_value=issue), patch.object(r, 'pages', return_value=[comment(work_id, 0)]):
            result = r.refresh_votes({work_id: {}}, registry, previous)
        self.assertEqual(result['works'][work_id]['votes'], 0)
        self.assertEqual(result['status'], 'ok')

    def test_failed_votes_do_not_become_zero(self):
        previous = {'observed_at': 'old', 'works': {'a': {'votes': 5}}}
        with patch.object(r, 'github', side_effect=ValueError('bad API')):
            result = r.refresh_votes({}, {'repository': r.REPOSITORY, 'issue_number': 1}, deepcopy(previous))
        self.assertEqual(result['works']['a']['votes'], 5)
        self.assertEqual(result['observed_at'], 'old')
        self.assertEqual(result['status'], 'stale')

    def test_manual_initialization_guard(self):
        with patch.dict(r.os.environ, {'GITHUB_ACTIONS': ''}):
            with self.assertRaises(ValueError):
                r.initialize_votes({})

    def test_initialization_recovers_existing_comments_without_duplicates(self):
        first, second = 'a' * 16, 'b' * 16
        works = {key: {'name': key, 'url': 'https://example.com', 'category': 'Games', 'audit': 'Pending'} for key in (first, second)}
        issue = {'number': 12, 'state': 'open', 'html_url': 'https://github.com/test/issues/12',
                 'body': r.ISSUE_MARKER, 'user': {'login': r.BOT, 'type': 'Bot'}}
        with patch.dict(r.os.environ, {'GITHUB_ACTIONS': 'true', 'GITHUB_REPOSITORY': r.REPOSITORY}), \
                patch.object(r, 'pages', side_effect=[[issue], [comment(first)]]), \
                patch.object(r, 'write_json'), patch.object(r.time, 'sleep'), patch.object(r, 'github') as api:
            registry = r.initialize_votes(works)
        self.assertEqual(registry['issue_number'], 12)
        api.assert_called_once()
        self.assertEqual(api.call_args[0][:2], ('/issues/12/comments', 'POST'))
        self.assertIn(r.ballot_marker(second), api.call_args[0][2]['body'])

    def test_auth_is_only_sent_to_github(self):
        with patch.dict(r.os.environ, {'GITHUB_TOKEN': 'test-only-not-a-secret'}), patch.object(r.urllib.request, 'build_opener') as opener:
            opener.return_value.open.side_effect = ValueError('stop before request')
            for url, should_auth in [('https://api.github.com/repos/a/b', True), ('https://api.fxtwitter.com/status/1', False)]:
                with self.assertRaises(ValueError):
                    r.request_json(url)
                req = opener.return_value.open.call_args[0][0]
                self.assertEqual(req.has_header('Authorization'), should_auth)


if __name__ == '__main__':
    unittest.main()
