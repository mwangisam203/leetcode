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



#Valid Anagram
#Problem: Given two strings, check if one is a rearrangement of the other.

from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False



#4: Group Anagrams
#Problem: Given a list of strings, group the ones that are anagrams of each other.

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))   # anagrams share the same sorted form
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


##5: Product of Array Except Self
##Problem: Return an array where each element is the product of all other elements (no division allowed).

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

print(product_except_self([1, 2, 3, 4]))  # [24, 12, 8, 6]


##RANDOM Practice

def containsDuplicates(alfs):
    seen = set()
    for alf in alfs:
        if alf in seen:
            return True
        seen.add(alf)
    return False

print(containsDuplicates(["ef", "abd", "cd", "abc", "dba"])) 


def hasDuplicates(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False

print(hasDuplicates([23, 30, 12, 1, 0, 30, 12, 50, 90, 0]))

