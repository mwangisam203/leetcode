"""Compare window algorithms with small, direct reference solutions."""
import unittest

from Arrays.arrays import max_window_sum
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
