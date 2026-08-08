def twoSum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i
    return False
