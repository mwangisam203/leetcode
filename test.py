def Anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or char == 0:
            return False
        count[char] -= 1
    return True


def my_anagram(s, t):
    if len(s) != len(t):
            return False

    CountS, CountT = {}, {}
    for i in range (len(s)):
        CountS[s[i]] = 1 + CountS.get(s[i], 0)
        CountT[t[i]] = 1 + CountT.get(t[i], 0)
    return CountS == CountT

