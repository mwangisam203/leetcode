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


class Solution:
    def two_summ(self, nums, target):

        seen = {}
        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [seen[value], i]
            seen[num] = i
        return False


print(Solution().two_summ([2, 7, 9, 11], target=9))



def twosum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i


print(twosum([2, 7, 8, 11,15], target=9))

## Brute force approach 1 (sorting:)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("adc", "dac"))    


'''
Idea: sorting rearranges both strings into a canonical (fixed) order. If they're anagrams, sorting makes them identical strings.
Time complexity: O(n log n) — sorting dominates.
Space complexity: O(n) — sorted() returns a new list; you're not sorting in place.'''



## Brute force approach 2 . (nested loop "cross out")
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



# TWO SUM

'''
"Given an array of integers `nums` and an integer `target`, return the indices of
the two numbers that add up to `target`. You may assume each input has exactly one
solution, and you may not use the same element twice. Return the answer in any order."
 
Interviewer follow-up you should expect: "Can you do better than O(n^2)?"
 
SOLUTION: '''

class Soluton:
    def twoSum(self, nums, target):
        seen ={}

        for i, num in enumerate (len(nums)):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i







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




'''
3. GROUP ANAGRAMS
---------------------------------------------------------------------
"Given an array of strings `strs`, group the anagrams together. You can return
the answer in any order. An anagram is a word formed by rearranging the letters
of another, using all the original letters exactly once."
 
Interviewer follow-up: "Is there a way to build the grouping key without sorting
each string?" (answer: yes — a character-count tuple/signature works too, and is
faster for long strings, O(k) instead of O(k log k) per string)
 
SOLUTION:
```python
'''

from collections import defaultdict
 
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())   ##Time: O(n * k log k), k = avg string length · Space: O(n * k)

''' FIRST NON-REPEATING CHARACTER
---------------------------------------------------------------------
"Given a string `s`, find the first non-repeating character in it and return its
index. If it does not exist, return -1."
 
Interviewer follow-up: "Can you do this without a second pass?" (usually not
cleanly — two passes is the accepted answer here: one to count, one to check order)
 
SOLUTION:
```python '''

from collections import Counter
 
def first_unique_char(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
###Time: O(n) · Space: O(1) (bounded alphabet)


'''
5. SUBARRAY SUM EQUALS K
---------------------------------------------------------------------
"Given an array of integers `nums` and an integer `k`, return the total number
of contiguous subarrays whose elements sum to `k`."
 
Interviewer follow-up: "The brute force is O(n^2) — can you get to O(n)?" This is
the moment they're checking if you know the prefix-sum-plus-hashmap trick.
 
SOLUTION:
```python
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
          ##Time: O(n) · Space: O(n)

'''
6. LONGEST CONSECUTIVE SEQUENCE
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence. You must write an algorithm that runs in O(n) time."
 
Interviewer follow-up: "The 'O(n) time' constraint in the prompt is a hint — sorting
would be O(n log n), so they want you to recognize that constraint rules out sorting."
 
SOLUTION:
```python
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

'''
7. VALID ANAGRAM
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and
false otherwise."
 
Interviewer follow-up: "Can you do it without using Counter/a library function?"
(expect to write the manual counting version too)
 
SOLUTION:
```python'''

from collections import Counter
 
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
    return True   ### Time: O(n) · Space: O(1) bounded alphabet





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





'''
8. TOP K FREQUENT ELEMENTS
---------------------------------------------------------------------
HOW IT'S ASKED:
"Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order."

Interviewer follow-up: "Sorting by frequency is O(n log n) — can you do better?"
This is where bucket sort (index = frequency) gets you to O(n).'''


from collections import Counter
 
def top_k_frequent(nums, k):
    counts = Counter(nums)
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


'''
9. INTERSECTION OF TWO ARRAYS
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

            #Time: O(n + m) · Space: O(n + m)



'''
10. DESIGN HASHMAP
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
```python'''

class MyHashMap:
    def __init__(self, size=1000):
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
            ##Time: O(1) average, O(n) worst case per operation · Space: O(n)



from collections import defaultdict

class Solution:
    def groupAnagram(strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()


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
            # counting freq of each string
            freqCount = [0] * 26
            
            for char in s: 
                freqCount[ord(char) - ord('a')] += 1
            res[tuple(freqCount)].append(s)
        return list(res.values())



def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False




def hasduplicates(words):

    seen = set()

    for word in words:
        if word in seen:
            return True
        seen.add(word)
        
    return False

print(hasduplicates(["eat", "tea", "eat"]))


from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    for s in strs:
        count = 0 * 26

        for c in s:
            ord[c] - ord["a"] += 1
        res[tuple(count)].append(s)
    return list(res.values())



def contdupli(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


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




def twoSum(nums, target):

    viewed = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in viewed:
            return [viewed[complement], i]
        viewed[num] = i
    return False

print(twoSum([2, 7, 9, 11, 12], target=9))


from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    #res = defaultdict(list)

    for s in strs:
            # counting freq of each string
        Count = [0] * 26
            
        for char in s: 
            Count[ord(char) - ord('a')] += 1
        res[tuple(Count)].append(s)
    return list(res.values())


print(groupAnagram(["act","pots","tops","cat","stop","hat"]))


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       
        results = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a, b , .. z

            for c in s:
                count[ord(c) - ord("a")] += 1

            results[tuple(count)].append(s)

        return list(results.values())

from collections import defaultdict

def groupanagram(strs):

    res = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)

    return list(res.values())



def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return False
