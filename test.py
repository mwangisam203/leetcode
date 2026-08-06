from collections import defaultdict

class Solution:
    def groupAnagram(strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = defaultdict(list)

        for i in range(len(strs)):
            code = [0] * 26
            for c in strs[i]:
                code[ord(c) - ord('a')] += 1
            groups[tuple(code)].append(strs[i])
        
        return list(groups.values())


    

def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
