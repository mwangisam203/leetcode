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
