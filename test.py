def groupanagram(strs):
    res = {} # defaultdict

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("a")] += 1

        res[tuple(count)].append(word)

    return list(res.values())