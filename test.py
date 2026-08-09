from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    for s in strs:
        count = 0 * 26 # a .. z

        for c in s:
            ord(c) - ord("a") += 1
        res[tuple(count)].append(s)
    return list(res.values())


print(groupAnagram(["act","pots","tops","cat","stop","hat"]))
