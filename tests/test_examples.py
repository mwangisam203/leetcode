"""Exercise every practice definition, including names redefined later in a file."""
import ast
from collections import Counter
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from math import prod
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_variants():
    variants = []
    for relative in ('Arrays/arrays.py', 'Hashing/hashing.py', 'Notes.py', 'test.py'):
        path = ROOT / relative
        namespace = {'__name__': 'practice_examples'}
        tree = ast.parse(path.read_text(), filename=str(path))
        with redirect_stdout(StringIO()):
            for node in tree.body:
                exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), namespace)
                label = f'{relative}:{node.lineno}'
                if isinstance(node, ast.FunctionDef):
                    variants.append((label, node.name, namespace[node.name]))
                elif isinstance(node, ast.ClassDef):
                    cls = namespace[node.name]
                    if node.name == 'MyHashMap':
                        variants.append((label, node.name, cls))
                    else:
                        instance = cls()
                        for method in node.body:
                            if isinstance(method, ast.FunctionDef):
                                variants.append((label, method.name, getattr(instance, method.name)))
    return variants


VARIANTS = load_variants()
SMALL_ARRAYS = [list(items) for n in range(5) for items in product((-1, 0, 1), repeat=n)]


class ExampleTests(unittest.TestCase):
    def variants(self, predicate):
        matches = [(label, fn) for label, name, fn in VARIANTS if predicate(name.lower())]
        self.assertTrue(matches, 'No matching variants were tested')
        return matches

    def test_duplicate_checks(self):
        for label, fn in self.variants(lambda name: 'dup' in name and name not in ('find_all_duplicates', 'find_duplicate_floyd')):
            for values in SMALL_ARRAYS:
                with self.subTest(variant=label, values=values):
                    self.assertIs(fn(values.copy()), len(set(values)) < len(values))

    def test_two_sum(self):
        for label, fn in self.variants(lambda name: name in ('two_sum', 'twosum')):
            for values in SMALL_ARRAYS:
                for target in range(-2, 3):
                    with self.subTest(variant=label, values=values, target=target):
                        pairs = [(i, j) for i in range(len(values)) for j in range(i + 1, len(values)) if values[i] + values[j] == target]
                        result = fn(values, target)
                        if not pairs:
                            self.assertEqual(result, [])
                        else:
                            self.assertEqual(len(result), 2)
                            self.assertIn(tuple(sorted(result)), pairs)

    def test_valid_anagrams(self):
        cases = [('', '', True), ('', 'a', False), ('listen', 'silent', True), ('aab', 'abb', False), ('éa', 'aé', True), ('A', 'a', False)]
        for label, fn in self.variants(lambda name: 'anagram' in name and not name.startswith('group')):
            for s, t, expected in cases:
                with self.subTest(variant=label, s=s, t=t):
                    self.assertIs(fn(s, t), expected)

    def test_group_anagrams(self):
        for label, fn in self.variants(lambda name: name.startswith('group')):
            for words in ([], ['', ''], ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], ['a', 'a', 'aa', 'b']):
                with self.subTest(variant=label, words=words):
                    expected = {}
                    for word in words:
                        expected.setdefault(''.join(sorted(word)), []).append(word)
                    self.assertEqual(sorted(sorted(group) for group in fn(words)), sorted(sorted(group) for group in expected.values()))

    def test_minimum_and_maximum(self):
        for label, fn in self.variants(lambda name: name in ('minval', 'findmin', 'largest', 'find_min', 'find_min_manual')):
            for values in SMALL_ARRAYS[1:]:
                with self.subTest(variant=label, values=values):
                    expected = max(values) if fn.__name__ == 'largest' else min(values)
                    self.assertEqual(fn(values), expected)
            if label.startswith('Notes.py'):
                self.assertIsNone(fn([]))
            else:
                with self.assertRaises(ValueError):
                    fn([])

    def test_minimum_index_and_key(self):
        for _, fn in self.variants(lambda name: name == 'find_min_with_index'):
            self.assertIsNone(fn([]))
            self.assertEqual(fn([3, -1, -1]), (-1, 1))
        for _, fn in self.variants(lambda name: name == 'find_min_by_key'):
            self.assertIsNone(fn([], key=lambda item: item[1]))
            self.assertEqual(fn([('A', 85), ('B', 72)], key=lambda item: item[1]), ('B', 72))

    def test_sliding_window_minimum(self):
        for label, fn in self.variants(lambda name: name == 'sliding_window_min'):
            for values in SMALL_ARRAYS:
                for k in range(1, len(values) + 1):
                    with self.subTest(variant=label, values=values, k=k):
                        self.assertEqual(fn(values, k), [min(values[i:i + k]) for i in range(len(values) - k + 1)])
            for values, k in [([], 1), ([1], 0), ([1], -1), ([1], 2)]:
                with self.assertRaises(ValueError):
                    fn(values, k)

    def test_product_except_self(self):
        for _, fn in self.variants(lambda name: name == 'product_except_self'):
            for values in SMALL_ARRAYS:
                self.assertEqual(fn(values), [prod(values[:i] + values[i + 1:]) for i in range(len(values))])

    def test_subarray_sum(self):
        for _, fn in self.variants(lambda name: name == 'subarray_sum'):
            for values in SMALL_ARRAYS:
                for k in range(-2, 3):
                    self.assertEqual(fn(values, k), sum(sum(values[i:j]) == k for i in range(len(values)) for j in range(i + 1, len(values) + 1)))

    def test_longest_consecutive(self):
        for _, fn in self.variants(lambda name: name == 'longest_consecutive'):
            for values, expected in [([], 0), ([100, 4, 200, 1, 3, 2, 2], 4), ([-2, -1, 0, 2], 3), ([5, 5], 1)]:
                self.assertEqual(fn(values), expected)

    def test_frequencies_and_intersection(self):
        for _, fn in self.variants(lambda name: name == 'first_unique_char'):
            for s, expected in [('', -1), ('aabb', -1), ('leetcode', 0), ('loveleetcode', 2)]:
                self.assertEqual(fn(s), expected)
        for _, fn in self.variants(lambda name: name == 'intersection'):
            self.assertEqual(set(fn([1, 2, 2], [2, 3])), {2})
            self.assertEqual(fn([], [1]), [])
        for _, fn in self.variants(lambda name: name == 'find_all_duplicates'):
            self.assertEqual(set(fn([1, 2, 2, 3, 1])), {1, 2})
            self.assertEqual(fn([]), [])

    def test_top_k(self):
        for _, fn in self.variants(lambda name: name == 'top_k_frequent'):
            for values in SMALL_ARRAYS:
                counts = Counter(values)
                for k in range(len(counts) + 1):
                    result = fn(values, k)
                    self.assertEqual(len(set(result)), k)
                    self.assertEqual(len(result), k)
                    self.assertEqual(sorted([counts[x] for x in result], reverse=True), sorted(counts.values(), reverse=True)[:k])
            for k in (-1, 2):
                with self.assertRaises(ValueError):
                    fn([1], k)

    def test_floyd_duplicate(self):
        for _, fn in self.variants(lambda name: name == 'find_duplicate_floyd'):
            for n in range(1, 5):
                for values in product(range(1, n + 1), repeat=n + 1):
                    duplicates = [value for value, count in Counter(values).items() if count > 1]
                    if len(duplicates) == 1:
                        self.assertEqual(fn(values), duplicates[0])

    def test_hash_map(self):
        for _, cls in self.variants(lambda name: name == 'myhashmap'):
            for size in (0, -1):
                with self.assertRaises(ValueError):
                    cls(size)
            table = cls(1)  # Force every key into the same bucket.
            table.put(1, 10)
            table.put(2, 20)
            table.put(1, 11)
            self.assertEqual(table.get(1), 11)
            self.assertEqual(table.get(2), 20)
            table.remove(1)
            table.remove(99)
            self.assertEqual(table.get(1), -1)
            self.assertEqual(table.get(2), 20)


if __name__ == '__main__':
    unittest.main()
