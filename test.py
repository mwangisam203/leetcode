from collections import defaultdict

class Solution:
    def groupAnagram(strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                

