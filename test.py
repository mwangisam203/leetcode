
from collections import defaultdict

def groupanagram(strs):

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())

def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return False
        