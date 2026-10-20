# Top K Frequent, one step at a time

The task returns **distinct values**, ordered by decreasing frequency. It does
not return their counts or their positions. The implementation is
[`top_k_frequent`](../Hashing/hashing.py).

## List length, distinct values, and k

```python
nums = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7]
n = len(nums)       # 10 elements
u = len(set(nums))  # 7 distinct values
k = 2              # return two of those distinct values
```

Python gets the length from the list you pass. To use ten numbers, put ten values
in the list; no length setting in the function needs changing. Repeated values
still count toward `len(nums)`. This repo allows integer `k` from zero through
`u`: zero returns `[]`, and out-of-range values raise `ValueError`.

## Count, bucket, collect

For `nums = [1, 1, 2, 2, 3]`:

```text
counts = {1: 2, 2: 2, 3: 1}
buckets[0] = []
buckets[1] = [3]
buckets[2] = [1, 2]
```

The dictionary maps **number → frequency**. A bucket index is a frequency;
the values inside that bucket are numbers having that frequency.
No frequency can exceed `len(nums)`, so `len(nums) + 1` buckets are enough to
include index `len(nums)`. The implementation allocates only through the largest
observed frequency, which is 2 in this example.

Visit buckets from highest frequency down. For `k=1`:

| Step | Action | Result | Stop? |
| --- | --- | --- | --- |
| 1 | Open frequency bucket 2 | `[]` | No |
| 2 | Append value 1 | `[1]` | Yes: one value collected |

For `k=2`, append 2 next and return `[1, 2]`. Equal frequencies are ties;
either tied value is a valid choice when only one is needed. This implementation
visits tied values in their first-occurrence order.

## Why the indentation matters

```python
for frequency in range(len(buckets) - 1, 0, -1):
    for number in buckets[frequency]:
        result.append(number)
        if len(result) == k:
            return result
```

Check immediately after **each append**. A check outside the inner loop waits
until the entire bucket has been appended. With `k=1`, bucket `[1, 2]` takes the
length straight from 0 to 2. It never equals 1; without a final return, the
function falls through and returns `None`.

`range(start, stop, step)` excludes `stop`. For frequency indices, a stop of 0
and step of -1 includes frequency 1 and excludes the unused frequency 0.
`range(n, 0 - 1)` instead has two arguments: it means `range(n, -1)` with the
default positive step, which is empty when n is nonnegative.

## Practice checks

Predict each answer before running:

| Input | k | Expected |
| --- | --- | --- |
| `[1, 1, 2, 2, 3]` | 1 | `[1]` in this implementation |
| `[1, 1, 2, 2, 3]` | 2 | `[1, 2]` |
| `[7, 7, 7]` | 1 | `[7]` |
| `[]` | 0 | `[]` |
| `[7, 7, 7]` | 2 | `ValueError`: only one distinct value |

For a tied answer, check its length, uniqueness, and selected frequencies rather
than assuming every correct algorithm must pick the same tied values.
Counting and buckets take average O(n) time and O(n) space. Sorting the u unique
values instead takes O(n + u log u) time and O(u) space; it is another useful
reference approach. Neither approach changes `nums`.
