def top_k_frequent(nums, k):

    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, frequency in count.items():
        buckets[frequency].append(number)

    res = []

    for frequency in range(len(nums), 0, -1):
        for number in buckets[frequency]:
            res.append(number)

            if len(res) == k:
                return res


print(top_k_frequent([1,2,2,3,3,3], k=2))



def encoded(strs):
    parts = []

    for word in strs:
        parts.append(str(len(word)))
        parts.append("#")
        parts.append(word)

    return "".join(word)


def decode(encoded):

    results = []

    i = 0

    while i < len(encoded):
        j = i

        while encoded[j] != "#":
            j += 1

            length = int(encoded[i:j])
            start = j + 1
            end = start + length

            results.append(encoded[start:end])

            end = i

        return results

        

    

            
