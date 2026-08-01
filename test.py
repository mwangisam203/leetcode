
def hasDuplicates(words):
    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)
    return False

print(hasDuplicates(["apples", "apples"]))
    

def myAnagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
    return True
print(myAnagram("racecar", "carrace"))



def two_sum(nums, target):
    for i