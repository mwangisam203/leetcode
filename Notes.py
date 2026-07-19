def find_min(arr):
    if not arr:
        return None
    return min(arr)

def find_min_manual(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr[1:]:
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
    return min(items, key=key)

# example: list of (name, score) tuples, min by score
people = [("A", 85), ("B", 72), ("C", 90)]
lowest = find_min_by_key(people, key=lambda x: x[1])