"""Reference-based checks for additional array and hashing patterns."""
from collections import Counter
import unittest
from test_examples import SMALL_ARRAYS, VARIANTS


class PatternTests(unittest.TestCase):
    def fn(self, name):
        matches = [fn for _, candidate, fn in VARIANTS if candidate == name]
        self.assertEqual(len(matches), 1, name)
        return matches[0]

    def test_two_sum_sorted(self):
        fn = self.fn('two_sum_sorted')
        for values in SMALL_ARRAYS:
            values = sorted(values)
            for target in range(-2, 3):
                pairs = [(i, j) for i in range(len(values)) for j in range(i + 1, len(values)) if values[i] + values[j] == target]
                result = fn(values, target)
                if pairs:
                    self.assertIn(tuple(result), pairs)
                else:
                    self.assertEqual(result, [])

    def test_prefix_ranges(self):
        build, query = self.fn('prefix_sums'), self.fn('range_sum')
        for values in SMALL_ARRAYS:
            prefix = build(values)
            self.assertEqual(len(prefix), len(values) + 1)
            for start in range(len(values) + 1):
                for stop in range(start, len(values) + 1):
                    self.assertEqual(query(prefix, start, stop), sum(values[start:stop]))
        for start, stop in [(-1, 0), (1, 0), (0, 2)]:
            with self.assertRaises(ValueError):
                query(build([1]), start, stop)

    def test_move_zeroes(self):
        fn = self.fn('move_zeroes')
        for values in SMALL_ARRAYS:
            actual = values.copy()
            self.assertIsNone(fn(actual))
            self.assertEqual(actual, [x for x in values if x != 0] + [0] * values.count(0))

    def test_rotate_right(self):
        fn = self.fn('rotate_right')
        for values in SMALL_ARRAYS:
            for k in range(-6, 7):
                actual = values.copy()
                self.assertIsNone(fn(actual, k))
                offset = k % len(values) if values else 0
                expected = values[-offset:] + values[:-offset] if offset else values
                self.assertEqual(actual, expected)

    def test_merge_sorted(self):
        fn = self.fn('merge_sorted')
        for a in SMALL_ARRAYS[:40]:
            for b in SMALL_ARRAYS[:40]:
                left, right = sorted(a), sorted(b)
                self.assertEqual(fn(left, right), sorted(a + b))
                self.assertEqual(left, sorted(a))
                self.assertEqual(right, sorted(b))

    def test_max_subarray_sum(self):
        fn = self.fn('max_subarray_sum')
        with self.assertRaises(ValueError):
            fn([])
        for values in SMALL_ARRAYS[1:]:
            expected = max(sum(values[i:j]) for i in range(len(values)) for j in range(i + 1, len(values) + 1))
            self.assertEqual(fn(values), expected)

    def test_max_stock_profit(self):
        fn = self.fn('max_stock_profit')
        for values in SMALL_ARRAYS:
            prices = [x + 2 for x in values]
            expected = max([0] + [prices[j] - prices[i] for i in range(len(prices)) for j in range(i + 1, len(prices))])
            self.assertEqual(fn(prices), expected)
