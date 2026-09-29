from collections import defaultdict


def groupAnagram(strs):
    """Group anagrams made of lowercase English letters (a-z)."""

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26 # a...z

        for c in word:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())



def top_k_frequent(nums, k):

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    
