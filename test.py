
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

print(Solution().isAnagram("jar", "jam"))



class Solution:
    def itsAnagram(self, t, s):
        if len(t) != len(s):
            return False

        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1
        for char in s:
            if char not in count or count[char] == 0:
                return False
        return True

print(Solution().itsAnagram("car", "bar"))
    

