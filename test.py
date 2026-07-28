

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