def find_min(arr):
    if not arr:
        return None
    return min(arr)

def find_min_manual(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:  # Avoid allocating a slice.
        if num < smallest:
            smallest = num
    return smallest


def find_min_with_index(arr):
    if not arr:
        return None
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return arr[min_idx], min_idx


def find_min_by_key(items, key):
    return min(items, key=key, default=None)

# example: list of (name, score) tuples, min by score
people = [("A", 85), ("B", 72), ("C", 90)]
lowest = find_min_by_key(people, key=lambda x: x[1])

from collections import deque



def sliding_window_min(arr, k):
    """Return window minima; require 1 <= k <= len(arr)."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the array length")
    result = []
    dq = deque()  # stores indices, increasing value order
    for i, num in enumerate(arr):
        while dq and arr[dq[-1]] >= num:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result




from collections import deque

def sliding_window_min(arr, k):
    """Return window minima; require 1 <= k <= len(arr)."""
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the array length")
    result = []
    dq = deque()  # stores indices, increasing value order
    for i, num in enumerate(arr):
        while dq and arr[dq[-1]] >= num:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result




from collections import Counter

def find_all_duplicates(arr):
    counts = Counter(arr)
    return [num for num, c in counts.items() if c > 1]



def has_duplicates_sorted(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False

'''
Time: O(n log n) · Space: O(n): sorted() creates a copy and sorting uses workspace.
For already sorted input, scan it directly in O(n) time and O(1) extra space.
'''



def find_duplicate_floyd(arr):
    # Preconditions: n+1 integers in [1, n], with exactly one distinct
    # duplicated value (which may appear more than twice).
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow2 = arr[0]
    while slow2 != slow:
        slow2 = arr[slow2]
        slow = arr[slow]
    return slow

'''
Time: O(n) · Space: O(1) — no extra data structure at all
This is a special-case trick (LeetCode 287 "Find the Duplicate Number"). 
Only works under those exact constraints. Worth knowing because it's a favorite "can you avoid extra space" follow-up.
'''
