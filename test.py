def twosum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return False

print(twosum([2, 7 , 8, 9], target=9))