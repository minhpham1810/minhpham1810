import unittest
import xml.etree.ElementTree as ET

from contributions import render_svg, update_readme, normalize


class ContributionTests(unittest.TestCase):
    def test_merge_is_distinct_from_closed(self):
        pr = {'base': {'repo': {'full_name': 'a/b'}}, 'number': 1,
              'title': 'Fix <XML> & data', 'html_url': 'https://github.com/a/b/pull/1',
              'state': 'closed', 'merged_at': None, 'updated_at': '2026-11-04'}
        self.assertEqual(normalize(pr)['state'], 'closed')
        pr['merged_at'] = '2026-11-04'
        self.assertEqual(normalize(pr)['state'], 'merged')

    def test_svg_handles_untrusted_titles_and_empty_data(self):
        for prs in ([], [{'repo': 'a/b', 'number': 1, 'state': 'open',
                         'title': '<script> & "quotes" ' * 30,
                         'url': 'https://github.com/a/b/pull/1', 'updated_at': '2026-11-04'}]):
            for theme in ('dark', 'light'):
                svg = render_svg({'pull_requests': prs, 'updated_at': '2026-11-04'},
                                 {'projects': {}, 'summaries': {}}, theme)
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg')
                self.assertNotIn('<script>', svg)

    def test_readme_preserves_surrounding_sections(self):
        original = '# Intro\nKeep exactly.\n\n## Open-source contributions\n\nOld\n\n## Highlighted projects\nKeep these too.\n'
        result = update_readme(original, 'New card\n')
        self.assertEqual(result, original.replace('Old\n', 'New card\n'))
        self.assertEqual(update_readme(result, 'New card\n'), result)
        with self.assertRaises(ValueError):
            update_readme('# No section', 'card')


if __name__ == '__main__':
    unittest.main()
