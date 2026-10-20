"""Extra practice: minimum helpers, a monotonic deque, and duplicate finding.

Minimum helpers return None on empty input. Other functions state their own
preconditions. Importing this module leaves demonstrations unexecuted.
"""
from collections import Counter, deque


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

# Example: select a (name, score) tuple by its score.
if __name__ == "__main__":
    people = [("A", 85), ("B", 72), ("C", 90)]
    print(find_min_by_key(people, key=lambda item: item[1]))


def sliding_window_min(arr, k):
    """Return minima for each window; require integer 1 <= k <= len(arr).

    O(n) time and O(k) workspace beyond output; input is unchanged.
    The deque contains candidate indices with increasing values. A newer value
    no larger than an old candidate dominates it and stays in the window longer.
    Each index is appended once and removed at most once across both ends.
    """
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
    """Find the duplicated integer using cycle detection without mutation.

    Requires n+1 integers in [1, n], exactly one distinct duplicated value;
    that value may appear more than twice. Preconditions are assumed, not checked.
    Outside this domain, indexing may fail or the loop may not terminate.
    O(n) time and O(1) extra space under these preconditions.
    """
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
