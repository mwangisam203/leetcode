## two_summ

class Solution:
    def two_summ(self, nums, target):

        seen = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [seen[value], i]
            seen[num] = i
        return False


print(Solution().two_summ([2, 7, 9, 11], target=9))



            

