import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('checker', Path(__file__).with_name('check_publication.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PublicationChecks(unittest.TestCase):
    def test_environment_terms(self):
        self.assertEqual(checker.load_private_terms(environ={'PUBLICATION_PRIVATE_TERMS': '["local-only"]'}), ['local-only'])

    def test_missing_policy_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                checker.load_private_terms(Path(folder), environ={})

    def test_explicit_generic_only(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(checker.load_private_terms(Path(folder), environ={}, allow_empty=True), [])

    def test_external_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'
            root.mkdir()
            policy = Path(folder) / 'private.json'
            policy.write_text('["local-only"]', encoding='utf-8')
            self.assertEqual(checker.load_private_terms(root, {'PUBLICATION_PRIVATE_TERMS_FILE': str(policy)}), ['local-only'])

    def test_invalid_policy_does_not_echo_value(self):
        for value in ['secret-value', '{}', '[1]', '[]', '[""]']:
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as error:
                    checker.load_private_terms(environ={'PUBLICATION_PRIVATE_TERMS': value})
                self.assertNotIn(value, str(error.exception))

    def test_case_insensitive_terms(self):
        self.assertTrue(checker.has_private_reference('LOCAL-ONLY', ['local-only']))

    def test_generic_windows_path(self):
        self.assertTrue(checker.has_private_reference('C:' + '\\' + 'Users' + '\\' + 'sample', []))

    def test_links_source_and_redaction(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'entry.md').write_text('[file](space%20name.md)\nlocal-only', encoding='utf-8')
            (root / 'space name.md').write_text('ok', encoding='utf-8')
            errors, count = checker.check_source(root, ['local-only'])
            self.assertEqual(count, 2)
            self.assertEqual(len(errors), 1)
            self.assertNotIn('local-only', errors[0])


if __name__ == '__main__':
    unittest.main()
