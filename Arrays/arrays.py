"""Array/list practice, grouped by problem and implementation technique.

Sections: minimum/maximum; contains duplicate; valid anagram; product except self.
Set/dictionary versions of duplicates and anagrams live in Hashing/hashing.py.
Repeated function and Solution names are standalone practice variants; running
this file executes their nearby examples, and later definitions replace earlier ones.
"""


# ============================================================================
# 1. Minimum and maximum values
# ============================================================================
# Linear scans: O(n) time, O(1) extra space; these examples require nonempty lists.

# Checking minimum values
values = [64, 36]
values.append(30)
values.append(24)
values.append(13)
values.append(5)
values.append(1)

print("My added list: ", values)

# The append calls above build [64, 36, 30, 24, 13, 5, 1].

number = values[0]

for i in values:

    if i < number:
        number = i

print(number)
print("My list: ", values)


numbers = [20, 45, 87, 12, 49, 25, 0, 13]

smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num
print("smallest number is: ", smallest_number)


my_cart = [23, 9, 13, 6, 18, 1, 25, 2]

smallest_number = my_cart[0]

for num in my_cart:
    if num < smallest_number:
        smallest_number = num
print(smallest_number)


def minVal(myArray):
    if not myArray:
        raise ValueError("minimum requires a nonempty list")

    minVal = myArray[0]

    for i in myArray:
        if i < minVal:
            minVal = i

    return minVal


print(minVal([100, 250, 23, 50, 0]))


class Solution:
    def findMin(self, nums):
        if not nums:
            raise ValueError("minimum requires a nonempty list")
        minimum = nums[0]

        for num in nums:
            if num < minimum:
                minimum = num
        return minimum

#solution = Solution()
#ans = solution.findMin([13, 3, 5, 2])
# print(ans) , or
print(Solution().findMin([13, 3, 5, 2]))


class Answer:

    def largest(self, digits: list[int]) -> int:
        if not digits:
            raise ValueError("maximum requires a nonempty list")

        largest = digits[0]

        for large in digits:
            if large > largest:
                largest = large
        return largest

# solve = Answer()
# Ans = solve.largest([12, 8, 5, 50])
# print(Ans)

print(Answer().largest([8,4,10,2]))


# ============================================================================
# 2. Contains Duplicate — sorting and list scans
# ============================================================================
# Set/dictionary alternatives: Hashing/hashing.py, Contains Duplicate.

#Contains Duplicate

# Sorting variant: O(n log n) time; modifies the input list.
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False



def containDuplicates(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
print(containDuplicates([1,4,3, 1,3]))


def contain_duplicates(nums):

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


##Brute force approach

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
# Time complexity: O(n²)
# Space complexity: O(1)
'''
The brute force checks every pair of elements, which is O(n²) — that's my starting point, but I can do better by trading space for time using a hash set, bringing it down to O(n) time at the cost of O(n) space.'''


# Another sorting variant:
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
    # Time complexity: O(n log n)
    # Space complexity: O(n) worst-case auxiliary space for Python's list.sort().
'''
Why this is "better than brute force but not the best": once sorted, any duplicates become adjacent to each other, so you only need one pass to find them.
The hash-set approach has better average asymptotic time since it avoids the log n factor and doesn't require mutating the input.'''


def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# List membership variants: O(n²) time and O(n) extra space.


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


def my_duplicates(words):
    viewed = []
    for word in words:
        if word in viewed:
            return True
        viewed.append(word)
    return False

print(my_duplicates(["xyz", "ghj", "vbh", "xyz"]))


def containDups(nums):
    seen = []

    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

print(containDups([1, 4, 7, 90, 1, 5]))


# ============================================================================
# 3. Anagrams — sorting and list removal
# ============================================================================
# Frequency-counting and Group Anagrams examples: Hashing/hashing.py, Anagrams.

## Sorting approach
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("adc", "dac"))


'''
Idea: sorting rearranges both strings into a canonical (fixed) order. If they're anagrams, sorting makes them identical strings.
Time complexity: O(n log n) — sorting dominates.
Space complexity: O(n) — sorted() returns a new list; you're not sorting in place.'''


# Brute-force approach: scan and remove matching characters
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    t_list = list(t)
    for char in s:
        if char in t_list:
            t_list.remove(char)
        else:
            return False
    return True

'''
Time complexity: O(n²) — char in t_list is an O(n) scan through a list,
and .remove() is also O(n) (it has to shift elements).
Doing this for every character in s (n characters) gives O(n²) total.
Space complexity: O(n) — the copy t_list.'''


# ============================================================================
# 4. Product of Array Except Self
# ============================================================================
# Prefix/suffix products: O(n) time, O(1) extra space excluding the output.

# Product of Array Except Self
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
