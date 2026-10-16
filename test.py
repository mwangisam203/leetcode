class Solution:
    def two_sum(nums, target):

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if num in seen:
                return [seen[complement], i]
            seen[num] = i

        return False

        