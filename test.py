class Solution:
    def anagram(self, s, t):

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

solution = Solution()


ans = solution.anagram(s= "bom", t="mpb")
print(ans)
