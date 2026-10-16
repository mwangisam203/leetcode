def twosum(nums, target):
    seen = {}

    for num in nums:
        diff = target - num

        if num in seen:
    