# TWO SUM

'''
"Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`. You may assume each input has exactly one
solution, and you may not use the same element twice. Return the answer in any order."
 
Interviewer follow-up you should expect: "Can you do better than O(n^2)?"
 
SOLUTION: '''


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  #Time: O(n) · Space: O(n)


'''
2. CONTAINS DUPLICATE
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given an integer array `nums`, return true if any value appears at least twice
in the array, and return false if every element is distinct."
 
Interviewer follow-up: "Can you do this in a single pass?" / "What if I ask for
which value is duplicated, not just true/false?"
'''

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False         #Time: O(n) · Space: O(n)