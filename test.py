def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[ complement], i]
        seen[num] = i

print(two_sum([3,4,5,6], 7))

    



























































from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

#Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


def groupanagram(strs):
    results = defaultdict(list)

    for s in strs:
        count = [0] * 26 # a....z




