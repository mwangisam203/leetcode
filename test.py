def twosum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return 

print(twosum([4, 3, 2, 5, 6], target=9))
    