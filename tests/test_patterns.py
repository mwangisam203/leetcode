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

    def test_nearby_duplicates(self):
        fn = self.fn('contains_nearby_duplicate')
        for values in SMALL_ARRAYS:
            for k in range(-1, 6):
                expected = any(values[i] == values[j] and j - i <= k for i in range(len(values)) for j in range(i + 1, len(values)))
                self.assertIs(fn(values, k), expected)

    def test_multiset_intersection(self):
        fn = self.fn('intersection_multiset')
        for left in SMALL_ARRAYS[:40]:
            for right in SMALL_ARRAYS[:40]:
                a, b = left.copy(), right.copy()
                self.assertEqual(Counter(fn(a, b)), Counter(left) & Counter(right))
                self.assertEqual((a, b), (left, right))

    def test_isomorphic_strings(self):
        fn = self.fn('is_isomorphic')
        words = ['', 'a', 'aa', 'ab', 'aba', 'abb', 'abc', 'éé', '猫犬']
        for s in words:
            for t in words:
                expected = len(s) == len(t) and all((s[i] == s[j]) == (t[i] == t[j]) for i in range(len(s)) for j in range(len(s)))
                self.assertIs(fn(s, t), expected)

    def test_word_pattern(self):
        fn = self.fn('word_pattern')
        for pattern, text, expected in [('abba', 'dog cat cat dog', True), ('abba', 'dog cat cat fish', False), ('ab', 'dog dog', False), ('aa', 'dog cat', False), ('', '  ', True), ('a', '', False), ('ab', '  dog\tcat\n', True)]:
            self.assertIs(fn(pattern, text), expected)

    def test_longest_zero_sum(self):
        fn = self.fn('longest_zero_sum_subarray')
        for values in SMALL_ARRAYS:
            expected = max([0] + [j - i for i in range(len(values)) for j in range(i + 1, len(values) + 1) if sum(values[i:j]) == 0])
            self.assertEqual(fn(values), expected)

    def test_unicode_anagram_groups(self):
        fn = self.fn('group_anagrams_unicode')
        words = ['éa', 'aé', '猫犬', '犬猫', '', '', 'A', 'a', 'é', 'e\u0301']
        expected = [['éa', 'aé'], ['猫犬', '犬猫'], ['', ''], ['A'], ['a'], ['é'], ['e\u0301']]
        self.assertEqual(sorted(map(sorted, fn(words))), sorted(map(sorted, expected)))

    def test_top_k_sorted(self):
        fn = self.fn('top_k_frequent_sorted')
        for values in SMALL_ARRAYS:
            counts = Counter(values)
            for k in range(len(counts) + 1):
                result = fn(values, k)
                self.assertEqual(len(result), k)
                self.assertEqual(len(set(result)), k)
                self.assertEqual(sorted([counts[x] for x in result], reverse=True), sorted(counts.values(), reverse=True)[:k])
        self.assertEqual(fn([3, 2, 1], 2), [3, 2])
        for k in (-1, 2):
            with self.assertRaises(ValueError):
                fn([1], k)
