def top_k(nums, k):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, frequency in counts.items():
        buckets[frequency].append(number)

    res = []

    for frequency in range(len(nums), 0, -1):
        for number in buckets[frequency]:
            res.append(number)

            if len(res) == k:
                return res

print(top_k([2, 2, 3, 3, 3, 8 ,3, 8, 8], k=2))