from collections import defaultdict


def groupAnagram(strs):

    res = defaultdict(list)

    for str in strs:
        count = [0] * 26 # a...z

        for c in str:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(str)

    return res.values



