class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

solution = Solution()

Solution.hasDuplicate(solution, [1, 4, 3, 1, 3])