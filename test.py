

def myAnagram(x, y):
    if len(x) != len(y):
        return False

    count = {}

    for char in count:
        if char in count:
            count[char] += 1

        else:
            count[char] = 1

        


print(myAnagram("adc", "bdc"))          
