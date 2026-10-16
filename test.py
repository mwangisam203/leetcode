from collections import defaultdict

class Solution:
    def groupAnagram(self, strs):

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())


solution = Solution()
strs = ["act","pots","tops","cat","stop","hat"]

results = solution.groupAnagram(strs)
print(results)







