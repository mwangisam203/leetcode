from itertools import product
import unittest

from Stacks.stacks import daily_temperatures, valid_parentheses
from tests.helpers import SMALL_ARRAYS


class StackTests(unittest.TestCase):
    def test_brackets_against_pair_reduction(self):
        for size in range(5):
            for chars in product('()[]{}', repeat=size):
                text = ''.join(chars)
                reduced = text
                while True:
                    next_text = reduced.replace('()', '').replace('[]', '').replace('{}', '')
                    if next_text == reduced:
                        break
                    reduced = next_text
                with self.subTest(text=text):
                    self.assertIs(valid_parentheses(text), reduced == '')

    def test_bracket_contract_and_deep_nesting(self):
        for text in ['a', '(a)', ' ', '([)]', ']', '(((']:
            self.assertFalse(valid_parentheses(text), text)
        self.assertTrue(valid_parentheses('(' * 1000 + ')' * 1000))

    def test_warmer_days_against_forward_scans(self):
        for values in SMALL_ARRAYS + [[70, 70, 72, 69], [73, 74, 75, 71, 69, 72, 76, 73]]:
            before = values.copy()
            expected = [next((j - i for j in range(i + 1, len(values))
                              if values[j] > temperature), 0)
                        for i, temperature in enumerate(values)]
            with self.subTest(values=values):
                self.assertEqual(daily_temperatures(values), expected)
                self.assertEqual(values, before)
