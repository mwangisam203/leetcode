def twosum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        compliment = target - num

        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i

    return []
