"""Reference-based checks for additional array and hashing patterns."""
from collections import Counter
import unittest
from tests.helpers import SMALL_ARRAYS, VARIANTS


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

    def test_move_zeroes_preserves_nonzero_objects(self):
        fn = self.fn('move_zeroes')
        first, second = 1.5, 2.5
        values = [first, second, 0, 0]
        alias = values
        self.assertIsNone(fn(values))
        self.assertIs(values, alias)
        self.assertIs(values[0], first)
        self.assertIs(values[1], second)
        self.assertEqual(values, [1.5, 2.5, 0, 0])

    def test_nearby_duplicate_window_boundaries(self):
        fn = self.fn('contains_nearby_duplicate')
        self.assertFalse(fn(list(range(1000)) + [0], 999))
        self.assertTrue(fn(list(range(1000)) + [0], 1000))
        self.assertTrue(fn([1, 2, 3, 1, 1], 1))
        self.assertFalse(fn([1, 2, 1, 2], 1))

    def test_multiset_intersection_unbalanced_inputs(self):
        fn = self.fn('intersection_multiset')
        large = [1] * 1000 + [2] * 500
        for left, right in [(large, [2, 1, 2]), ([2, 1, 2], large), (large, []), ([], large)]:
            self.assertEqual(Counter(fn(left, right)), Counter(left) & Counter(right))

    def test_hash_map_collision_deletions(self):
        class Key:
            def __init__(self, value):
                self.value = value
            def __hash__(self):
                return 0
            def __eq__(self, other):
                return isinstance(other, Key) and self.value == other.value
        table = self.fn('MyHashMap')(1)
        for i in range(5):
            table.put(Key(i), i * 10)
        for removed in (0, 2, 4):
            table.remove(Key(removed))
            self.assertEqual(table.get(Key(removed)), -1)
        self.assertEqual(table.get(Key(1)), 10)
        self.assertEqual(table.get(Key(3)), 30)
        table.remove(Key(99))

    def test_hash_map_entry_count(self):
        table = self.fn('MyHashMap')(2)
        self.assertEqual(len(table), 0)
        table.put(1, 0)
        table.put(1, 100)
        table.put(3, -1)
        self.assertEqual(len(table), 2)
        table.remove(99)
        self.assertEqual(len(table), 2)
        table.remove(1)
        table.remove(1)
        self.assertEqual(len(table), 1)
        table.remove(3)
        self.assertEqual(len(table), 0)

    def test_hash_map_growth_preserves_entries(self):
        table = self.fn('MyHashMap')(2)
        for key in range(100):
            table.put(key, key * 7)
            self.assertLessEqual(len(table) / table.size, 0.75)
        self.assertGreater(table.size, 2)
        capacity = table.size
        for key in range(100):
            self.assertEqual(table.get(key), key * 7)
            table.put(key, -key)
        self.assertEqual(table.size, capacity)
        self.assertEqual(len(table), 100)
        for key in range(100):
            self.assertEqual(table.get(key), -key)
        for key in range(100):
            table.remove(key)
        self.assertEqual(len(table), 0)
        self.assertEqual(table.size, capacity)

    def test_hash_map_mixed_operations_against_dict(self):
        from random import Random
        class Key(int):
            def __hash__(self):
                return 0
        rng = Random(20261013)
        table = self.fn('MyHashMap')(2)
        expected = {}
        for _ in range(1000):
            key = Key(rng.randrange(-20, 21))
            operation = rng.choice(['put', 'get', 'remove'])
            if operation == 'put':
                value = rng.randrange(-100, 101)
                table.put(key, value)
                expected[key] = value
            elif operation == 'remove':
                table.remove(key)
                expected.pop(key, None)
            else:
                self.assertEqual(table.get(key), expected.get(key, -1))
            self.assertEqual(len(table), len(expected))
            for stored_key, value in expected.items():
                self.assertEqual(table.get(stored_key), value)

    def test_array_operations_on_larger_inputs(self):
        from random import Random
        rng = Random(42)
        rotate = self.fn('rotate_right')
        merge = self.fn('merge_sorted')
        prefix = self.fn('prefix_sums')
        product_except_self = self.fn('product_except_self')
        for _ in range(20):
            values = [rng.randrange(-10, 11) for _ in range(50)]
            original = values.copy()
            alias = values
            k = rng.randrange(-10000, 10001)
            rotate(values, k)
            self.assertIs(values, alias)
            rotate(values, -k)
            self.assertEqual(values, original)
            sums = prefix(values)
            self.assertEqual([sums[i + 1] - sums[i] for i in range(len(values))], values)
            self.assertEqual(merge(sorted(values[:25]), sorted(values[25:])), sorted(values))
            self.assertEqual(values, original)
        self.assertEqual(product_except_self([0, 2, 3]), [6, 0, 0])
        self.assertEqual(product_except_self([0, 0, 3]), [0, 0, 0])
        huge = 10 ** 30
        self.assertEqual(product_except_self([huge, 2, -3]), [-6, -3 * huge, 2 * huge])
