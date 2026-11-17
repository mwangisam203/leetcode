from collections import defaultdict

def groupanagram(strs):

    res = defaultdict(list)

    for word in strs:
        counts = [0] * 26 #a....z

        for char in word:
            counts[ord(char) - ord("a")] += 1

            res[tuple(counts)].append(word)

    return list(res.values())