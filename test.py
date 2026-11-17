def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []

nums = [4,4,5,6]
target = 7

print(two_sum(nums, target))