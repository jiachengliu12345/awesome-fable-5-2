import json
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import rankings as r
import readme_rankings as h

ROOT = Path(__file__).resolve().parents[1]


class ReadmeRankingsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = json.loads((ROOT / 'data/rankings.json').read_text())
        self.registry = json.loads((ROOT / 'data/voting.json').read_text())
        self.before = {}
        for filename in h.LANGUAGES.values():
            self.before[filename] = (ROOT / filename).read_text()
            (self.root / filename).write_text(self.before[filename])

    def render(self, votes=None):
        with patch.object(r, 'ROOT', self.root), patch.object(r, 'request_json', side_effect=AssertionError('offline generation made a network call')):
            r.render(self.data['works'], self.data['sources'], self.registry, votes or self.data['votes'])

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_generation_preserves_catalog_and_is_repeatable(self):
        self.render()
        first = self.snapshot()
        self.render()
        self.assertEqual(first, self.snapshot())
        for filename in h.LANGUAGES.values():
            before, after = self.before[filename], (self.root / filename).read_text()
            self.assertEqual(before.split(h.START)[0], after.split(h.START)[0])
            self.assertEqual(before.split(h.END)[1], after.split(h.END)[1])
        audit = (ROOT / 'CODE-AUDIT.md').read_text()
        old_catalog = r.catalog(self.before['README.md'], audit)
        new_catalog = r.catalog((self.root / 'README.md').read_text(), audit)
        self.assertEqual(old_catalog, new_catalog)

    def test_all_picture_variants_exist_are_valid_and_keep_source_scope(self):
        self.render()
        svgs = list((self.root / h.ASSETS).glob('*.svg'))
        self.assertEqual(len(svgs), 48)
        for path in svgs:
            tree = ET.parse(path)
            svg = tree.getroot()
            self.assertNotIn('nan', path.read_text().lower())
            paired = path.name.startswith('platforms-')
            mobile = '-mobile' in path.name
            self.assertEqual(svg.attrib['width'], '480' if mobile else ('984' if paired else '840'))
            self.assertIsNotNone(svg.find('{http://www.w3.org/2000/svg}desc'))
            if paired:
                cards = svg.findall('{http://www.w3.org/2000/svg}svg')
                self.assertEqual(len(cards), 2)
                self.assertEqual([card.attrib['x'] for card in cards], ['0', '0' if mobile else '504'])
                self.assertEqual(cards[0].attrib['y'], '0')
                self.assertEqual(cards[1].attrib['y'], str(int(cards[0].attrib['height']) + 16) if mobile else '0')
                for card in cards:
                    self.assertLessEqual(int(card.attrib['y']) + int(card.attrib['height']), int(svg.attrib['height']))
                ids = [node.attrib['id'] for node in svg.iter() if 'id' in node.attrib]
                self.assertEqual(len(ids), len(set(ids)))
            for node in svg.findall('{http://www.w3.org/2000/svg}text'):
                self.assertLess(float(node.attrib['y']), float(svg.attrib['height']))
        for filename in h.LANGUAGES.values():
            readme = (self.root / filename).read_text()
            section = readme.split(h.START)[1].split(h.END)[0]
            for path in re.findall(r'(?:src|srcset)="([^"]+)"', section):
                self.assertTrue((self.root / path).is_file(), path)
            self.assertIn('assets/rankings/platforms-', section)
            self.assertNotIn('src="assets/rankings/x-', section)
            self.assertNotIn('src="assets/rankings/github-', section)
            self.assertEqual(section.count('<details>'), 1)
            self.assertEqual(section.count('</details>'), 1)
            self.assertIn('Fable 5.2 FPS Reproduction', section)
            self.assertIn('Rainy Dock Materials', section)
            self.assertIn('Hard-Surface Modeling Studio', section)
        gh = (self.root / h.ASSETS / 'github-en-light.svg').read_text()
        self.assertIn('Cached; refresh failed', gh)
        self.assertIn('shared by 3 works', gh)
        youtube = (self.root / h.ASSETS / 'youtube-en-light.svg').read_text()
        self.assertIn('overview / comparison', youtube)
        self.assertIn('README snapshot', youtube)

    def test_missing_markers_do_not_partially_update_readmes(self):
        chinese = self.before['README.zh-CN.md'].replace(h.END, '')
        (self.root / 'README.zh-CN.md').write_text(chinese)
        with self.assertRaisesRegex(ValueError, 'markers'):
            self.render()
        self.assertEqual((self.root / 'README.md').read_text(), self.before['README.md'])
        self.assertEqual((self.root / 'README.zh-CN.md').read_text(), chinese)
        self.assertFalse((self.root / h.ASSETS).exists())
        for bad in [h.START + h.START + h.END, h.END + h.START]:
            with self.assertRaises(ValueError):
                h.replace_preview(bad, 'new')

    def test_svg_escapes_content_and_handles_zero_and_empty_rows(self):
        rows = [{'rank': 1, 'label': 'A < B & "C" 中文' * 4, 'value': 0, 'note': 'old & cached'}]
        svg = h.svg_card('Test & <title>', 'subtitle', rows, ('empty', 'detail'), 'en', 'dark', True, 'x')
        tree = ET.fromstring(svg)
        self.assertEqual(tree.find('{http://www.w3.org/2000/svg}title').text, 'Test & <title>')
        bars = tree.findall('{http://www.w3.org/2000/svg}rect')
        self.assertFalse(any(b.attrib.get('height') == '8' and b.attrib['fill'] == '#58a6ff' for b in bars))
        empty = h.svg_card('X', 'No sources', [], ('No measured sources yet', 'Unknown is not zero.'), 'en', 'light', False, 'x')
        self.assertIn('Unknown is not zero.', empty)
        self.assertNotIn('>01<', empty)

    def test_vote_states_and_positive_top_five_share_full_ranking_order(self):
        ids = list(self.data['works'])[:7]
        self.registry['issue_url'] = 'https://github.com/test/repo/issues/1'
        votes = {'status': 'ok', 'observed_at': '2026-11-12T10:00:00Z', 'works': {
            key: {'votes': count, 'url': f'https://github.com/test/repo/issues/1#issuecomment-{n}'}
            for n, (key, count) in enumerate(zip(ids, [10, 10, 7, 5, 2, 2, 0]))}}
        self.render(votes)
        section = (self.root / 'README.md').read_text().split('### Reader choice')[1].split(h.END)[0]
        expected = list(r.ranked([(self.data['works'][i]['name'], i) for i in ids], lambda item: votes['works'][item[1]]['votes']))[:5]
        self.assertEqual(re.findall(r'\*\*(\d+)\.\*\*', section), [str(rank) for rank, _ in expected])
        for _, (_, work_id) in expected:
            self.assertIn(votes['works'][work_id]['url'], section)
        self.assertNotIn(votes['works'][ids[-1]]['url'], section)
        for status, expected_text in [('not_initialized', 'Voting is not open yet'), ('unavailable', 'Vote totals are unavailable'), ('closed', 'Voting issue is closed'), ('ok', 'No votes in this snapshot yet')]:
            state = {**votes, 'status': status, 'works': {i: {**v, 'votes': 0} for i, v in votes['works'].items()}}
            self.render(state)
            image = (self.root / h.ASSETS / 'readers-en-light.svg').read_text()
            self.assertIn(expected_text, image)
            self.assertNotIn('>01<', image)
        stale = deepcopy(votes)
        stale['status'] = 'stale'
        self.render(stale)
        section = (self.root / 'README.md').read_text().split('### Reader choice')[1].split(h.END)[0]
        self.assertIn('2026-11-12 10:00:00 UTC', section)
        self.assertIn('Cached; refresh failed', section)
        self.assertIn('**10**', section)


if __name__ == '__main__':
    unittest.main()
