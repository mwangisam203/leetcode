def twosum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i


print(twosum([2, 7, 8, 11,15], target=9))

## Brute force approach 1 (sorting:)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("adc", "dac"))    



def itsAnagram(a, b):

    if len(a) != len(b):
        return False

    count = {}

    for char in a:
        count[char] = count.get(char, 0) + 1

    for char in b:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print(itsAnagram("sam", "mam"))