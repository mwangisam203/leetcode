from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    #res = defaultdict(list)

    for s in strs:
            # counting freq of each string
        Count = [0] * 26
            
        for char in s: 
            Count[ord(char) - ord('a')] += 1
        res[tuple(Count)].append(s)
    return list(res.values())


print(groupAnagram(["act","pots","tops","cat","stop","hat"]))


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a, b , .. z

            for c in s:
                count[ord(c) - ord("a")] += 1

            results[tuple(count)].append(s)

        return list(results.values())