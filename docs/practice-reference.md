# Arrays and hashing reference

Current files:

- [Arrays](../Arrays/arrays.py): scans, sorting, two pointers, prefix sums, in-place operations, and running optima.
- [Hashing](../Hashing/hashing.py): sets, frequency counting, prefix lookups, string mappings, and hash map design.
- [Array notes](../Arrays/arrays.txt) and [hashing notes](../Hashing/hashing.txt).
- [Additional examples](../Notes.py), [scratch practice](../test.py), and [summary table](../Gennotes.txt).
- [Original example checks](../tests/test_examples.py) and [additional pattern checks](../tests/test_patterns.py).

Run all checks with `python3 -m unittest discover -s tests -v`.
Repeated definitions are independent practice variants; the checks capture each
one before a later definition replaces it. The 26-slot character-count grouping
variants assume a-z; group_anagrams_unicode supports arbitrary code points.
Min/max helpers in arrays.py reject empty lists; Notes.py minimum helpers return
None. Window sizes must be valid; Two Sum returns [] when no pair exists.

## Practice progression

Try each example before reading its implementation. State the input constraints,
write a small reference solution, then explain why the optimized version works.
The new functions have unique names so you can call them independently.

| Array exercise | Function | Key idea | Time | Extra space beyond output |
| --- | --- | --- | --- | --- |
| Two Sum on sorted input | `two_sum_sorted` | Move the pointer that can improve the sum | O(n) | O(1) |
| Repeated range sums | `prefix_sums`, `range_sum` | Subtract two prefixes | O(n) build, O(1) query | O(1) beyond the O(n) prefix result |
| Move Zeroes | `move_zeroes` | Compact nonzero values in order | O(n) | O(1) |
| Rotate Array | `rotate_right` | Reverse the whole list, then both parts | O(n) | O(1) |
| Merge Sorted Arrays | `merge_sorted` | Consume the smaller remaining value | O(n + m) | O(1) |
| Maximum Subarray | `max_subarray_sum` | Extend the current sum or restart | O(n) | O(1) |
| Single stock trade | `max_stock_profit` | Keep the cheapest earlier price | O(n) | O(1) |

`move_zeroes` and `rotate_right` mutate their list and return None; the other new
array functions preserve their inputs. Two Sum indices are **zero-based** here,
including the sorted variant (LeetCode 167 instead asks for one-based indices).
`range_sum` uses a half-open interval `[start, stop)` and requires a prefix array
created by `prefix_sums`. Negative rotation counts rotate left. Maximum Subarray
requires nonempty input; stock profit returns zero for empty or falling prices.

| Hashing exercise | Function | Key idea | Average time | Space including output |
| --- | --- | --- | --- | --- |
| Contains Duplicate II | `contains_nearby_duplicate` | Keep a bounded membership window | O(n) | O(min(n, k)) |
| Intersection II | `intersection_multiset` | Count the smaller input and consume matches | O(n + m) | O(min(n, m)) |
| Isomorphic Strings | `is_isomorphic` | Enforce mappings in both directions | O(n) | O(u) |
| Word Pattern | `word_pattern` | Map characters to whitespace-separated words | O(p + t) | O(p + t) |
| Longest zero-sum interval | `longest_zero_sum_subarray` | Preserve the earliest index of each prefix | O(n) | O(n) |
| Unicode Group Anagrams | `group_anagrams_unicode` | Use unordered character-count signatures | O(c + w) | O(c + w) |
| Top K by sorting | `top_k_frequent_sorted` | Sort distinct values by frequency | O(n + u log u) | O(u) |

Here n and m are input lengths, u is the number of distinct values or characters,
p and t are pattern/text lengths, and c and w are total characters/word count.
Hash-based bounds assume average constant-time table operations.

Compare these related examples in hashing.py:

- Duplicate detection versus nearby duplicates: the latter expires membership outside
  the preceding k positions, bounding storage by the window size.
- Set intersection versus multiset intersection: the latter keeps repeated matches.
- Subarray sum count versus longest zero-sum interval: store prefix frequencies for counting,
  but earliest indices for maximum length. Both support negative numbers.
- Sorted and 26-slot anagram keys versus Unicode signatures: Unicode grouping is
  case-sensitive and does not normalize visually equivalent code points.
- Bucket-based Top K versus sorting: buckets take O(n) time and space; sorting uses
  O(u) space and costs O(u log u) after counting. Both accept k=0 and reject k>u.
  The sorting variant skips sorting when k=0.

The test suite runs the original variants and these additions. It checks small
arrays exhaustively for many patterns, plus mutation contracts, invalid ranges,
Unicode strings, frequency ties, and hash-map collisions. Additional checks compare
mixed map operations with Python's dict and test larger arrays with reproducible seeds.

Implementation details to study:

- Move Zeroes skips self-swaps when a value is already in the right position.
- Nearby duplicates keeps only the preceding k values; k<=0 returns False.
- Multiset intersection counts the shorter input and drops exhausted counts.
  Its output order is unspecified; compare multiplicities rather than list order.
- `len(MyHashMap())` reports entries, while `.size` reports bucket capacity.
  Updating an existing key does not change the entry count. Missing-key removal
  does nothing, and `get` still returns -1 for missing keys.
- MyHashMap doubles its capacity when its load factor exceeds 0.75, rehashing
  existing entries. Insertions have amortized expected O(1) cost; a single growth
  operation scans the old buckets and entries. Adversarial collisions can still
  cause linear operations. Deletion does not shrink the table.

Run the checks with:

```bash
python3 -m unittest discover -s tests -v
```

## Follow-up practice on the same patterns

These examples sit beside related problems in the existing files.

| Function | File | What to explain before coding |
| --- | --- | --- |
| `pivot_index` | Arrays/arrays.py | Why subtract the current value from the right-hand sum? |
| `compact_sorted` | Arrays/arrays.py | Why is only the returned prefix meaningful? |
| `sorted_squares` | Arrays/arrays.py | Why can the largest square be at either end? |
| `majority_element` | Hashing/hashing.py | Why is the threshold strictly greater than half? |
| `first_repeated_value` | Hashing/hashing.py | Why does [1, 2, 2, 1] return 2? |
| `count_sum_pairs` | Hashing/hashing.py | Why count complements before storing the current value? |
| `subarrays_divisible_by_k` | Hashing/hashing.py | Why do equal prefix remainders identify divisible sums? |
| `longest_common_prefix` | Arrays/arrays.py | Why scan only as far as the shortest word? |
| `longest_consecutive_sorted` | Arrays/arrays.py | Why skip duplicate values without resetting the run? |

The new array scans take O(n) time except consecutive sorting (O(n log n)) and
common-prefix comparison (O(n * m), with m the shortest word length). Common-prefix
comparison also scans the n word lengths, so an empty shortest word still costs O(n).
Sorted Squares allocates its output; sorted consecutive runs allocate a copy.
Compaction mutates its input; its suffix is unspecified. Other new array functions
preserve input. The new hash-based scans take O(n) average time; they store distinct
values or remainders. Majority and first-repeat return None when absent.
Divisibility requires positive integer k and supports negative array values.

String codecs now reject missing separators, invalid length headers, and truncated
payloads with ValueError. Lengths count Python characters, not encoded bytes.
A # inside a payload is valid. Both the standalone and class codecs are checked
for round trips and cross-compatibility in [review tests](../tests/test_review.py).

Two existing algorithms also use less temporary storage: Top K buckets stop at
the maximum observed frequency, and unique intersection stores only the smaller
input's distinct values. Intersection output order is unspecified.
