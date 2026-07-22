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