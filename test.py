
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