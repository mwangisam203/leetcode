

def top_k(nums, k):

    counts  = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, frequecy in counts.items():
        buckets[frequecy].append(number)

    results = []

    for frequency in range(len(nums), 0, -1):
        for number in buckets[frequency]:
            results.append(number)

            if len(results) == k:
                return results

print(top_k([3, 4, 4, 2, 6, 8, 8, 8 , 8, 7, 7, 7, 7, 3], k=2))