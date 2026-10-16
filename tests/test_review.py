"""Regression checks and reference answers for arrays and hashing practice."""
from collections import Counter
from itertools import product
import unittest
from test_examples import SMALL_ARRAYS, VARIANTS


class ReviewTests(unittest.TestCase):
    def fn(self, name):
        matches = [fn for _, candidate, fn in VARIANTS if candidate == name]
        self.assertEqual(len(matches), 1, name)
        return matches[0]

    def test_decoders_reject_malformed_streams(self):
        decoders = [fn for _, name, fn in VARIANTS if name == 'decode']
        self.assertEqual(len(decoders), 2)
        for decode in decoders:
            for encoded in ['3abc', '#abc', '-1#a', '+1#a', 'x#a', '2#a', '1#a2#b', '1#a!', '١#a']:
                with self.subTest(encoded=encoded), self.assertRaises(ValueError):
                    decode(encoded)
