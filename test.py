from collections import defaultdict

class Solution:
    def groupAnagram(strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")]

            result[tuple(count)].append(s)

        return result.values()



def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
