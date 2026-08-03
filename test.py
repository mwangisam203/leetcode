def Anagram(s, t):
    if len(s) != len(t):
        return False

    CountS = {}
    CountT = {}

    for i in range (len(s)):
        CountS[s[i]] = 1 + CountS.get(s[i], 0)
        CountT[t[i]] = 1 + CountT.get(t[i], 0)
    return CountS == CountT

print(Anagram("team", "meat"))