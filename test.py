

## check if given string contain duplicates


def hasduplicates(words):
    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)
    return False

print(hasduplicates(["names", "name", "name"]))


## checking a valid anagram in a string e.g silent(s) == listen(t)

#solution

def itsAnagram(t, s):
    if len(s) != len(t):
        return False

    count = {}

    for char in t:
        count[char] = count.get(char, 0) + 1
    for char in s:
        