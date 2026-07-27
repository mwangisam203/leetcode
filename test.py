myarray = []

myarray.append(42)
myarray.append(2)
myarray.append(4)
myarray.append(12)
myarray.append(1)


minVar = myarray[0]

for i in myarray:
    if i < minVar:
        minVar = i

print(minVar)



def hasDuplicates(words):
    seen  = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)

    return False

print(hasDuplicates(["apple", "mango", "apple"]))