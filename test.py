def twosum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        # Look for the partner, not the current number; check before storing.
        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []  # No pair adds up to target.

print(twosum([4, 3, 2, 5, 6], target=9))
