#Contains Duplicate

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:      # O(1) check
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False


#Two Sum

##Given an array and a target, return the indices of two numbers that add up to the target.

def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]