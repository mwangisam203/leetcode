
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
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return  True

print(itsAnagram("anagram", "nagaram"))




def validAnagram(a, b):
    if len(a) == len(b):
        return True

    count = {}

    for char in a:
        count[char] = count.get(char, 0) + 1
    for char in b:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print(validAnagram("maiza", "amaize"))

def myAnagram(x, y):
    if len(x) != len(y):
        return False

    count = {}

    for char in x:
        if char in count:
            count[char] += 1

        else:
            count[char] = 1

    for char in y:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

        


print(myAnagram("adc", "dac"))          



def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(myAnagram("adc", "dab"))          
