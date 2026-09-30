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


def top_k(nums, k):

    count = {}

    for candidate in nums:
        frequency = 0

        for num in nums:
            if num == candidate:
                frequency += 1
            count[candidate] = frequency
            
        

    ranked = sorted(count, key=count.get, reverse=True)

    return ranked [:k]



def top_k_frequent(nums, k):

    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, frequency in counts.items():
        buckets[frequency].append(number)

    result =[]

    for frequency in range(len(nums), 0, -1):
        for number in buckets[frequency]:
            result.append(number)

            if result == k:
                return result





def encoded(strs):

    parts = []

    for word in strs:
        parts.append(str(len(word)))
        parts.append("#")
        parts.append(word)

    return "".join(parts)

def decode(encoded):

    res = []

    i = 0

    while i < len(encoded):
        


