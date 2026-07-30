def validAnagram(t, s):
    if len(t) != len(s):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count == 0:
            return False
        count[char] -= 1

    return True
print(validAnagram("jess", "jess"))