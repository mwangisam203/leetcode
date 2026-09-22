nums = [1, 2, 3, 4]

def contains_duplicates_brute_force(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

print(contains_duplicates_brute_force(nums))

#def conta

def contains_duplicate(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_duplicate(nums))
        
        
