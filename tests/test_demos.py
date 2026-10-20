"""Check the runnable learning examples through their command-line interface."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DemoTests(unittest.TestCase):
    def run_demo(self, *arguments):
        return subprocess.run(
            [sys.executable, '-m', 'examples.top_k', *arguments], cwd=ROOT,
            capture_output=True, text=True, timeout=10,
        )

    def test_default_ten_numbers(self):
        result = self.run_demo()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('length: 10; distinct: 7; k: 2', result.stdout)
        self.assertIn('top 2: [1, 2]', result.stdout)

    def test_tied_bucket_stops_at_k(self):
        result = self.run_demo('1', '1', '2', '2', '3', '-k', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('bucket[2]: [1, 2]', result.stdout)
        self.assertIn('top 1: [1]', result.stdout)

    def test_invalid_k_has_friendly_error(self):
        for k in ('-1', '2'):
            result = self.run_demo('7', '7', '-k', k)
            self.assertEqual(result.returncode, 2)
            self.assertIn('number of unique values', result.stderr)
            self.assertNotIn('Traceback', result.stderr)
