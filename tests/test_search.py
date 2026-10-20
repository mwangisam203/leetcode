from bisect import bisect_left
import unittest

from Search.search import binary_search, lower_bound
from tests.helpers import SMALL_ARRAYS


class SearchTests(unittest.TestCase):
    def test_search_against_membership(self):
        for values in SMALL_ARRAYS:
            nums = sorted(values)
            before = nums.copy()
            for target in range(-2, 3):
                with self.subTest(nums=nums, target=target):
                    index = binary_search(nums, target)
                    if target in nums:
                        self.assertGreaterEqual(index, 0)
                        self.assertLess(index, len(nums))
                        self.assertEqual(nums[index], target)
                    else:
                        self.assertEqual(index, -1)
                    self.assertEqual(nums, before)

    def test_lower_bound_against_bisect(self):
        for values in SMALL_ARRAYS:
            nums = sorted(values)
            before = nums.copy()
            for target in range(-2, 3):
                with self.subTest(nums=nums, target=target):
                    index = lower_bound(nums, target)
                    self.assertEqual(index, bisect_left(nums, target))
                    self.assertTrue(all(x < target for x in nums[:index]))
                    self.assertTrue(all(x >= target for x in nums[index:]))
                    self.assertEqual(nums, before)
