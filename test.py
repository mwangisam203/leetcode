
from collections import defaultdict

def groupanagram(strs):

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())