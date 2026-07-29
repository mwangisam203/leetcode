

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