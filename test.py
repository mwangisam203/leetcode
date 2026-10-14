def encode(strs):
    parts = []

    for s in strs:
        parts.append(str(len(s)))
        parts.append("#")
        parts.append(s)

    return "".join(parts)

    #parts += str(len(s)) + "#" + s

def decode(encode):
    res = []
    i = 0

    while i < len(encode):
        j = i

        while encode[j] != "#":
            j += 1

            length = int(len(encode[i:j]))
            start = j + 1 
            end  = start + length

            end = i

        res.append(encode[start:end])

    return res

print

        


