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

    def test_codecs_round_trip_and_interoperate(self):
        encoders = [fn for _, name, fn in VARIANTS if name == 'encode']
        decoders = [fn for _, name, fn in VARIANTS if name == 'decode']
        self.assertEqual(len(encoders), 2)
        self.assertEqual(len(decoders), 2)
        cases = [[], [''], ['', ''], ['#', '12#', '\n'], ['猫', '🙂', 'e\u0301'], ['x' * 1000, '', '#']]
        for encode in encoders:
            self.assertEqual(encode(['cat', '']), '3#cat0#')
            for words in cases:
                before = words.copy()
                encoded = encode(words)
                self.assertEqual(words, before)
                for decode in decoders:
                    self.assertEqual(decode(encoded), words)

    def test_top_k_on_sparse_and_dense_frequencies(self):
        fn = self.fn('top_k_frequent')
        self.assertEqual(set(fn(list(range(1000)), 1000)), set(range(1000)))
        self.assertEqual(fn([7] * 1000 + [2] * 10, 1), [7])
        self.assertEqual(fn([], 0), [])
