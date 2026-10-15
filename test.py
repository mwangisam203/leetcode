def encode(strs):
    parts = []

    for s in strs:
        parts.append(str(len(s)))
        parts.append("#")
        parts.append(s)

    return "".join(parts)


def decode(encoded):
    res = []
    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

        length = int(encoded[i:j])
        start = j + 1 
        end  = start + length

        i = end

        res.append(encoded[start:end])

    return res

strs = ["hello", "wo$rl#", "##"]


encoded = encode(strs)
decode = decode(encoded)

print(encoded)
print(decode)

        


class Solution:
    def encode(self, strs):
        parts = []


        for word in strs:
            parts.append(str(len(word)))
            parts.append("#")
            parts.append(word)

        return "".join(parts)

    def decode(self, encoded):
        result = []
        i = 0

        while i < len(encoded):
            j = i

            while encoded[j] != "#":
                j += 1

            length = int(encoded[i:j])
            start = j + 1
            end = start + length

            i = end

            result.append(encoded[start:end])

        return result


solution  = Solution()

strs = ["craig", "", "$5dafh#"]

encoded = solution.encode(strs)
decode =solution.decode(encoded)


print(encoded)
print(decode)
