"""Search sorted ascending sequences without modifying them.

Both functions assume the input is sorted; checking that would take O(n).
The active search interval is half-open: [left, right).
"""


def binary_search(nums, target):
    """Return a zero-based matching index or -1; any duplicate match is valid.

    O(log n) time, O(1) extra space. Empty input returns -1.
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


def lower_bound(nums, target):
    """Return the first index with value >= target, or len(nums) if absent.

    O(log n) time, O(1) extra space. Empty input returns 0.
    With duplicate targets, return the first occurrence.
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
