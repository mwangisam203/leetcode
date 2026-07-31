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

my_cart = [23, 9, 13, 6, 18, 1, 25, 2]

smallest_number = my_cart[0]

for num in my_cart:
    if num < smallest_number:
        smallest_number = num
print(smallest_number)


def minVal(myArray):
    myArray = [20, 23, 14, 37, 4]

    minVal = myArray[0]

    for i in myArray:
        if i < minVal:
            return minVal 


print(minVal)