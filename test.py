def twosum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i


print(twosum([2, 7, 8, 11,15], target=9))