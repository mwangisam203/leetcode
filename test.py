def twosum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        compliment = target - num

        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i

    return []
print(twosum([2, 7, 8, 9], target=9))




def top_k(nums, k):

    counts  = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for number, frequecy in counts.items():
        buckets[frequecy].append(number)

    results = []

    for frequency in range(len(nums), 0 -1):
        for number in buckets[frequency]:
            results.append(number)

        if len(results) == k:
            return results

print(top_k([1, 1, 1, 2, 2, 3], k=2))