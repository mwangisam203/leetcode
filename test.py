def topK(nums, k):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, freq in counts.items():
        buckets[freq].append(number)

    res = []
    for freq in range(len(nums), 0, -1):
        for number in buckets[freq]:
            res.append(number)

            if len(res) == k:
                return res

nums = [1,2,2,3,3,3]
k = 2
print(topK(nums, k))