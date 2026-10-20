"""Compare window algorithms with small, direct reference solutions."""
from itertools import product
import unittest

from Arrays.arrays import max_window_sum
from Hashing.hashing import longest_unique_substring_length
from tests.helpers import SMALL_ARRAYS


class WindowTests(unittest.TestCase):
    def test_fixed_window_against_direct_sums(self):
        for values in SMALL_ARRAYS:
            for k in range(1, len(values) + 1):
                with self.subTest(values=values, k=k):
                    before = values.copy()
                    expected = max(sum(values[i:i + k])
                                   for i in range(len(values) - k + 1))
                    self.assertEqual(max_window_sum(values, k), expected)
                    self.assertEqual(values, before)

    def test_invalid_window_sizes(self):
        for values, k in [([], 1), ([], 0), ([1], 0), ([1], -1), ([1], 2)]:
            with self.subTest(values=values, k=k), self.assertRaises(ValueError):
                max_window_sum(values, k)

    def test_all_negative_window(self):
        self.assertEqual(max_window_sum([-8, -2, -3, -7], 2), -5)

    def test_unique_substrings_against_enumeration(self):
        for size in range(6):
            for chars in product('ab猫', repeat=size):
                text = ''.join(chars)
                expected = max(
                    (stop - start for start in range(len(text) + 1)
                     for stop in range(start, len(text) + 1)
                     if len(set(text[start:stop])) == stop - start),
                    default=0,
                )
                with self.subTest(text=text):
                    self.assertEqual(longest_unique_substring_length(text), expected)

    def test_unique_substring_shrink_boundaries(self):
        for text, expected in [('abba', 2), ('abcabcbb', 3), ('bbbbb', 1),
                               ('pwwkew', 3), ('Aa🙂A', 3), ('', 0)]:
            with self.subTest(text=text):
                self.assertEqual(longest_unique_substring_length(text), expected)
