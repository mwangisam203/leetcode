def encode(strs):
    parts = []

    for s in strs:
        parts.append(str(len(s)))
        parts.append("#")
        parts.append(s)

    return "".join(parts)

    #parts += str(len(s)) + "#" + s

def decode(encoded):
    res = []
    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

        length = int(len(encoded[i:j]))
        start = j + 1 
        end  = start + length

        i = end

        res.append(encoded[start:end])

    return res

print(decode(encode="4#star3#cat"))

        


