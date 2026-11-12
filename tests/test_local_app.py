import http.client
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import local_app


class LocalAppTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.snapshot = Path(self.temp.name) / 'snapshot.json'
        self.snapshot.write_text(json.dumps({
            'works': {'a': {'name': 'First'}, 'b': {'name': 'Second'}},
            'sources': {'test': {'platform': 'X', 'metrics': {'views': 7}, 'status': 'stale'}},
            'votes': {'status': 'not_initialized', 'works': {}}
        }))
        self.state = Path(self.temp.name) / 'state'
        self.server = local_app.make_server(0, self.state, self.snapshot)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_port
        self.origin = f'http://127.0.0.1:{self.port}'

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()

    def request(self, path='/api/data', body=None, cookie='', csrf='', origin=None, host=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.port, timeout=3)
        headers = {'Cookie': cookie}
        if host:
            headers['Host'] = host
        if body is not None:
            headers.update({'Origin': origin or self.origin, 'X-CSRF-Token': csrf, 'Content-Type': 'application/json'})
        connection.request('GET' if body is None else 'POST', path, body=None if body is None else json.dumps(body), headers=headers)
        response = connection.getresponse()
        content = response.read()
        result = (response.status, dict(response.getheaders()), json.loads(content) if response.getheader('Content-Type', '').startswith('application/json') else content)
        connection.close()
        return result

    def session(self):
        status, headers, data = self.request()
        self.assertEqual(status, 200)
        return headers['Set-Cookie'].split(';')[0], data['csrf']

    def test_votes_idempotent_withdraw_and_independent_visitors(self):
        first, csrf1 = self.session()
        second, csrf2 = self.session()
        for _ in range(2):
            status, _, data = self.request('/api/vote', {'work_id': 'a', 'voted': True}, first, csrf1)
            self.assertEqual(status, 200)
            self.assertEqual(data['local_votes']['totals']['a'], 1)
        _, _, data = self.request('/api/vote', {'work_id': 'a', 'voted': True}, second, csrf2)
        self.assertEqual(data['local_votes']['totals']['a'], 2)
        _, _, data = self.request('/api/vote', {'work_id': 'a', 'voted': False}, first, csrf1)
        self.assertEqual(data['local_votes']['totals']['a'], 1)
        self.assertEqual(data['local_votes']['mine'], [])
        self.assertEqual(data['votes']['status'], 'not_initialized')

    def test_votes_persist_on_reopen_and_do_not_modify_source(self):
        original = self.snapshot.read_bytes()
        cookie, csrf = self.session()
        self.request('/api/vote', {'work_id': 'b', 'voted': True}, cookie, csrf)
        reopened = local_app.App(self.state, self.snapshot)
        identity = cookie.split('=', 1)[1]
        self.assertEqual(reopened.payload(identity, csrf)['local_votes']['totals'], {'b': 1})
        self.assertFalse(reopened.session(identity)[2])
        self.assertEqual(self.snapshot.read_bytes(), original)

    def test_rejects_cross_origin_missing_token_and_unknown_work(self):
        cookie, csrf = self.session()
        body = {'work_id': 'a', 'voted': True}
        self.assertEqual(self.request('/api/vote', body, cookie, csrf, 'https://other.example')[0], 403)
        self.assertEqual(self.request('/api/vote', body, cookie)[0], 403)
        self.assertEqual(self.request('/api/vote', {'work_id': 'missing', 'voted': True}, cookie, csrf)[0], 400)
        self.assertEqual(self.request('/api/vote', {'work_id': 'a', 'voted': 'true'}, cookie, csrf)[0], 400)
        self.assertEqual(self.request(host='other.example')[0], 403)
        self.assertEqual(self.request(cookie=cookie)[2]['local_votes']['totals'], {})

    def test_only_serves_public_assets(self):
        for path in ['/', '/style.css', '/app.js']:
            status, _, content = self.request(path)
            self.assertEqual(status, 200)
            self.assertGreater(len(content), 0)
        for path in ['/.git/config', '/.local/votes.sqlite3', '/../README.md', '/scripts/local_app.py']:
            self.assertEqual(self.request(path)[0], 404)

    def test_refresh_is_single_flight_and_keeps_votes_separate(self):
        cookie, csrf = self.session()
        self.request('/api/vote', {'work_id': 'a', 'voted': True}, cookie, csrf)
        started, release, done = threading.Event(), threading.Event(), threading.Event()
        def refresh_sources(sources):
            started.set()
            release.wait(3)
            sources['test'].update(status='ok', metrics={'views': 8})
        real_refresh = self.server.app._refresh
        def wrapped():
            try:
                real_refresh()
            finally:
                done.set()
        with patch.object(local_app.rankings, 'catalog', return_value=(self.server.app.data['works'], {'test': {'platform': 'X', 'observed_at': None, 'metrics': {}, 'status': 'unavailable'}})), \
                patch.object(local_app.rankings, 'refresh_sources', side_effect=refresh_sources), \
                patch.object(self.server.app, '_refresh', side_effect=wrapped):
            self.assertEqual(self.request('/api/refresh', {}, cookie, csrf)[0], 202)
            self.assertTrue(started.wait(2))
            self.assertFalse(self.server.app.start_refresh())
            self.assertTrue(self.request(cookie=cookie)[2]['refresh']['running'])
            release.set()
            self.assertTrue(done.wait(3))
        payload = self.request(cookie=cookie)[2]
        self.assertFalse(payload['refresh']['running'])
        self.assertEqual(payload['sources']['test']['metrics']['views'], 8)
        self.assertEqual(payload['local_votes']['totals'], {'a': 1})
        self.assertTrue((self.state / 'rankings.json').exists())
        self.assertEqual(json.loads(self.snapshot.read_text())['sources']['test']['metrics']['views'], 7)

    def test_refresh_failure_leaves_previous_snapshot(self):
        with patch.object(local_app.rankings, 'catalog', side_effect=ValueError('bad source')):
            self.server.app._refresh()
        self.assertEqual(self.server.app.data['sources']['test']['metrics']['views'], 7)
        self.assertFalse(self.server.app.refresh['running'])
        self.assertIn('仍展示', self.server.app.refresh['message'])


if __name__ == '__main__':
    unittest.main()
