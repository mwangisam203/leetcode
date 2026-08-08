from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    for s in strs:
        count = 0 * 26

        for c in s:
            ord[c] - ord["a"] += 1
        res[tuple(count)].append(s)
    return list(res.values())



def contdupli(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def newAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True
