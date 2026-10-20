"""Importing practice helpers should not execute their demonstrations."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ImportTests(unittest.TestCase):
    def assert_quiet_import(self, module):
        result = subprocess.run(
            [sys.executable, '-c', f'import {module}'],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, '')
        self.assertEqual(result.stderr, '')

    def test_arrays_import(self):
        self.assert_quiet_import('Arrays.arrays')

    def test_hashing_import(self):
        self.assert_quiet_import('Hashing.hashing')

    def test_notes_import(self):
        self.assert_quiet_import('Notes')
