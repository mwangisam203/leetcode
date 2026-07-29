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



##Brute force approach

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
            ## Time complexity: O(n²)
            ## Space complexity: O(1)
'''
The brute force checks every pair of elements, which is O(n²) — that's my starting point, but I can do better by trading space for time using a hash set, bringing it down to O(n) time at the cost of O(n) space.'''

# second brute-force variant — sorting:
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
    # Time complexity: O(n log n)
    # Space complexity: O(1) or O(n) depending on the sort algorithm's implementation (Python's sort() is in-place, O(1) extra space
'''
Why this is "better than brute force but not the best": once sorted, any duplicates become adjacent to each other, so you only need one pass to find them.
but the hash set approach is still faster overall since it avoids the log n factor and doesn't require mutating the input.'''




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


def duplicateWords(words):
    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)

    return False

print(duplicateWords(["apple", "mangoes", "lemons", "pawpaw", "tomatoes"]))


##checking min values
values = [64, 36]
values.append(30)
values.append(24)
values.append(13)
values.append(5)
values.append(1)

print("My added list: ", values)

#values = [64, 36, 30, 24, 13, 5, 1] ## just trying modify by ignoring this list and use the appended one

number = values[0]

for i in values:

    if i < number:
        number = i

print(number)
print("My list: ", values)

## duplicates practice
def containDups(chars):

    seen = set()

    for char in chars:
        if char in seen:
            return True

        seen.add(char)

print(containDups(["abc", "cba", "abc"]))

## Complex example
Words = ["apples", "lemon", "mango", "orange", "avocado"]

def myDuplicates(Words):

    viewed = set()

    for word in Words:
        if word in viewed:
            return True
        viewed.add(word)
    return False

print(myDuplicates(Words))

def duplicateExist(vocas):

    seen = []
    for voca in vocas:
        if voca in seen:
            return True
        seen.append(voca)
    return False

print(duplicateExist([3, 3, 45, 30, 1, 0, 0,1]))

def contains_duplicate(nums):
    seen = []                  # <- list instead of set
    for num in nums:
        if num in seen:        # <- still works, but now O(n) per check
            return True
        seen.append(num)       # <- .append() instead of .add()
    return False

print(contains_duplicate(["subaru", "BMW", "benz", "volvo"]))



def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True       # storing a placeholder value, since we only care about the key
    return False


def contains_duplicate(nums):
    seen = []
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False


# test cases
print(contains_duplicate([1, 2, 3, 1]))        # True  - 1 repeats
print(contains_duplicate([1, 2, 3, 4]))        # False - all unique
print(contains_duplicate(["a", "b", "a"]))     # True  - works on strings too
print(contains_duplicate([]))                  # False - empty list, no duplicates possible
print(contains_duplicate([5]))                 # False - single item, nothing to duplicate



def containDuplicates(nums):
    my_basket = set()

    for num in nums:
        if num in my_basket:
            return True
        my_basket.add(num)
    return False

print(containDuplicates([12, 34, 8, 30, 0, 12]))   

def my_duplicates(words):
    viewed = []
    for word in words:
        if word in viewed:
            return True
        viewed.append(word)
    return False

print(my_duplicates(["xyz", "ghj", "vbh", "xyz"]))


numbers = [20, 45, 87, 12, 49, 25, 0, 13]

smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num
print("smallest number is: ", smallest_number)


def hasduplicates(words):
    viewed = set()

    for word in words:
        if word in viewed:
            return True
        viewed.add(word)

    return False

print(hasduplicates(["abc", "dsc", "kqq"]))


def containDups(nums):
    seen = []

    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

print(containDups([1, 4, 7, 90, 1, 5]))



my_cart = [23, 9, 13, 6, 18, 1, 25, 2]

smallest_number = my_cart[0]

for num in my_cart:
    if num < smallest_number:
        smallest_number = num
print(smallest_number)