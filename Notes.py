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