"""Hashing practice, grouped by problem and implementation technique.

Sections: contains duplicate; two sum; anagrams (valid, then grouped);
first unique character; top K frequent; subarray sum; longest consecutive;
intersection; hash map design.
List/sorting alternatives live in Arrays/arrays.py. Hash table operations have
O(1) average cost. Repeated names are standalone practice variants; later
definitions replace earlier ones, so keep example calls beside their definition.
"""

from collections import Counter, defaultdict


# ============================================================================
# 1. Contains Duplicate — hash sets and dictionaries
# ============================================================================
# O(n) average time, O(n) space. List/sorting alternatives: Arrays/arrays.py.

'''
CONTAINS DUPLICATE
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


# Hash-set variant: O(n) average time; leaves the input unchanged.
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:      # O(1) check
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False


# More hash-set practice

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


## duplicates practice
def containDups(chars):

    seen = set()

    for char in chars:
        if char in seen:
            return True

        seen.add(char)
    return False

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


def contains_duplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True       # storing a placeholder value, since we only care about the key
    return False


def containDuplicates(nums):
    my_basket = set()

    for num in nums:
        if num in my_basket:
            return True
        my_basket.add(num)
    return False

print(containDuplicates([12, 34, 8, 30, 0, 12]))


def hasduplicates(words):
    viewed = set()

    for word in words:
        if word in viewed:
            return True
        viewed.add(word)

    return False

print(hasduplicates(["abc", "dsc", "kqq"]))


def hasduplicates(words):

    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)

    return False

print(hasduplicates(["eat", "tea", "eat"]))


def contdupli(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ============================================================================
# 2. Two Sum — complement lookup
# ============================================================================
# All variants store value -> index: O(n) average time, O(n) space.
# Return [] if no pair exists; never reuse the same index.

#Two Sum

##Given an array and a target, return the indices of two numbers that add up to the target.

def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No matching pair.

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]


class Solution:
    def two_sum(self, nums, target):

        seen = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [seen[value], i]
            seen[num] = i
        return []  # No matching pair.


print(Solution().two_sum([2, 7, 9, 11], target=9))


def twosum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i
    return []  # No matching pair.


print(twosum([2, 7, 8, 11,15], target=9))


# TWO SUM

'''
"Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`. You may assume each input has exactly one
solution, and you may not use the same element twice. Return the answer in any order."

Interviewer follow-up you should expect: "Can you do better than O(n^2)?"

SOLUTION: '''

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []  # No matching pair.


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No matching pair.


def twoSum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i
    return []  # No matching pair.

print(twoSum([2, 7, 9, 11, 12], target=9))


def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No matching pair.


# ============================================================================
# 3. Anagrams
# ============================================================================
# Valid Anagram examples come first, followed by all Group Anagrams variants.

# 3a. Valid Anagram — frequency counting


#Valid Anagram
#Problem: Given two strings, check if one is a rearrangement of the other.


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("rat", "car"))        # False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

print(Solution().isAnagram("jar", "jam"))


##valid anagram

def Anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True


print(Anagram("eat", "ete"))

# Two frequency dictionaries: still O(n) average time.
def my_anagram(s, t):
    if len(s) != len(t):
        return False

    CountS, CountT = {}, {}
    for i in range(len(s)):
        CountS[s[i]] = 1 + CountS.get(s[i], 0)
        CountT[t[i]] = 1 + CountT.get(t[i], 0)
    return CountS == CountT


print(my_anagram("eat", "ete"))


def validAnagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print(validAnagram("money", "nemoy"))


#example 2:

def itsAnagram(a, b):

    if len(a) != len(b):
        return False

    count = {}

    for char in a:
        count[char] = count.get(char, 0) + 1

    for char in b:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print(itsAnagram("sam", "mam"))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


'''
VALID ANAGRAM
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and
false otherwise."

Interviewer follow-up: "Can you do it without using Counter/a library function?"
(expect to write the manual counting version too)

SOLUTION:
'''


def is_anagram(s, t):
    return Counter(s) == Counter(t)
'''
Manual version (often requested explicitly):
'''
def is_anagram_manual(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts or counts[ch] == 0:
            return False
        counts[ch] -= 1
    return True   # Time: O(n); space: O(u) for u distinct characters (O(1) for a fixed alphabet).


def newAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True


# 3b. Group Anagrams — sorted keys in a dictionary


# Group Anagrams
#Problem: Given a list of strings, group the ones that are anagrams of each other.


def group_anagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))   # anagrams share the same sorted form
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


'''
GROUP ANAGRAMS
---------------------------------------------------------------------
"Given an array of strings `strs`, group the anagrams together. You can return
the answer in any order. An anagram is a word formed by rearranging the letters
of another, using all the original letters exactly once."

Interviewer follow-up: "Is there a way to build the grouping key without sorting
each string?" (answer: yes — a character-count tuple/signature works too, and is
faster for long strings, O(k) instead of O(k log k) per string)

SOLUTION:

'''


def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())   # Time: O(n * k log k), k = maximum word length; space: O(n * k + n).


# 3c. Group Anagrams — character-count tuple keys
# These 26-slot signatures assume lowercase English letters (a-z).


class Solution:
    def groupAnagram(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = defaultdict(list)

        for i in range(len(strs)):
            code = [0] * 26
            for c in strs[i]:
                code[ord(c) - ord('a')] += 1
            groups[tuple(code)].append(strs[i])

        return list(groups.values())


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list)

        for s in strs:
        # Count the frequency of each character.
            freqCount = [0] * 26

            for char in s:
                freqCount[ord(char) - ord('a')] += 1
            res[tuple(freqCount)].append(s)
        return list(res.values())


def groupAnagram(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())


def groupAnagram(strs):
    res = defaultdict(list)

    for s in strs:
        # Count the frequency of each character.
        Count = [0] * 26

        for char in s:
            Count[ord(char) - ord('a')] += 1
        res[tuple(Count)].append(s)
    return list(res.values())


print(groupAnagram(["act","pots","tops","cat","stop","hat"]))


'''
For the 26-slot signature, positions 0 through 25 correspond to a through z.
Only nonzero counts are shown here; each actual dictionary key is a full tuple.
"eat", "tea", "ate" -> a: 1, e: 1, t: 1 -> group A
"tan", "nat"        -> a: 1, n: 1, t: 1 -> group B
"bat"               -> a: 1, b: 1, t: 1 -> group C

Result: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]'''

def groupanagram(strs):

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())


# ============================================================================
# 4. First Non-Repeating Character
# ============================================================================
# Count characters, then scan in original order.

''' FIRST NON-REPEATING CHARACTER
---------------------------------------------------------------------
"Given a string `s`, find the first non-repeating character in it and return its
index. If it does not exist, return -1."

Interviewer follow-up: "Can you do this without a second pass?" (usually not
cleanly — two passes is the accepted answer here: one to count, one to check order)

SOLUTION:
 '''


def first_unique_char(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
# Time: O(n); space: O(u) for u distinct characters (O(1) for a fixed alphabet).


# ============================================================================
# 5. Top K Frequent Elements
# ============================================================================
# Frequency counting and buckets. Allow 0 <= k <= the number of unique values.

'''
TOP K FREQUENT ELEMENTS
--------------------------------------------------------------------------
HOW IT'S ASKED:
"Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order."

Interviewer follow-up: "Sorting by frequency is O(n log n) — can you do better?"
This is where bucket sort (index = frequency) gets you to O(n).'''


def top_k_frequent(nums, k):
    counts = Counter(nums)
    if not 0 <= k <= len(counts):
        raise ValueError("k must be between 0 and the number of unique values")
    if k == 0:
        return []
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result     #  Time: O(n) · Space: O(n)


# ============================================================================
# 6. Subarray Sum Equals K
# ============================================================================
# Prefix sums plus a dictionary of prefix frequencies.

'''
SUBARRAY SUM EQUALS K
---------------------------------------------------------------------
"Given an array of integers `nums` and an integer `k`, return the total number
of contiguous subarrays whose elements sum to `k`."

Interviewer follow-up: "The brute force is O(n^2) — can you get to O(n)?" This is
the moment they're checking if you know the prefix-sum-plus-hashmap trick.

SOLUTION:

'''
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}
    for num in nums:
        prefix_sum += num
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
# Time: O(n) average; space: O(n).


# ============================================================================
# 7. Longest Consecutive Sequence
# ============================================================================
# Hash-set membership finds sequence starts and extends them.

'''
LONGEST CONSECUTIVE SEQUENCE
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time."

Interviewer follow-up: "The 'O(n) time' constraint in the prompt is a hint — sorting
would be O(n log n), so they want you to recognize that constraint rules out sorting."

SOLUTION:

'''

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest       ##Time: O(n) · Space: O(n)


# ============================================================================
# 8. Intersection of Two Arrays
# ============================================================================
# Set intersection removes duplicates and finds shared values.

'''
INTERSECTION OF TWO ARRAYS
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given two integer arrays `nums1` and `nums2`, return an array of their
intersection. Each element in the result must be unique, and you may return
the result in any order."

Interviewer follow-up: "What if the arrays are sorted — does your approach
change?" (with sorted input, two pointers becomes a valid O(n+m) alternative
that uses O(1) extra space beyond the output)

SOLUTION:'''


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

# Time: O(n + m) average; space: O(n + m).


# ============================================================================
# 9. Design HashMap
# ============================================================================
# Buckets and separate chaining handle hash collisions.

'''
DESIGN HASHMAP
---------------------------------------------------------------------
HOW IT'S ASKED:
"Design a HashMap without using any built-in hash table libraries. Implement
the MyHashMap class with: `put(key, value)` — insert or update the value for a
key; `get(key)` — return the value for a key, or -1 if not found; `remove(key)`
— remove the key and its value if it exists."

Interviewer follow-up: "How do you handle collisions?" / "What's your load
factor strategy — would you resize?" This question exists specifically to test
whether you understand what dict/set do internally, not whether you can use them.

SOLUTION:
'''

class MyHashMap:
    def __init__(self, size=1000):
        if size <= 0:
            raise ValueError("hash map size must be positive")
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        idx = self._hash(key)
        self.buckets[idx] = [(k, v) for k, v in self.buckets[idx] if k != key]
# With n entries and b buckets: O(1 + n/b) expected time per operation,
# O(n) worst case; O(n + b) storage. This teaching implementation does not resize,
# so constant average time requires keeping the load factor n/b bounded.
