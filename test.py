

def myAnagram(x, y):
    if len(x) != len(y):
        return False

    count = {}

    for c in x:
        count[c] = count.get(c, 0) + 1

    for c in y:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1

    return True
        

        
print(myAnagram("adc", "dac"))