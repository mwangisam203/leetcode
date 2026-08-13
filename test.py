def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return False

print(two_sum([1, 3, 4, 7, 9], target=7))