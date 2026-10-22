def encode(strs):

    parts = []

    for word in strs:
        parts.append(str(len(word)))
        parts.append("#")
        parts.append(word)

    return "".join(parts)

# strs = (("fab", "", "amize"))
# print(encode(strs))

def decode(encoded):
    res = []
    i = [0]

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

            length = int(encoded[i:j])
            start  = j + 1
            end = start + len

            i = end

        res.append(encoded[start:end])

    return res

        
