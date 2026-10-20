# LeetCode practice

Python exercises and notes for learning how to choose an algorithm, explain its
invariant, and check its edge cases. Requires Python 3.10 or newer; no third-party
packages are needed. Run commands from this directory.

## Start here

1. Read the problem and constraints before opening its solution.
2. Write a simple correct solution, then identify repeated work.
3. Trace the optimized approach on a small input.
4. Check empty input, duplicates, negative values, and boundary indices.
5. Explain time, extra space, and whether the input changes.

```bash
python3 -m unittest discover -v
```

To run one check while practicing:

```bash
python3 -m unittest tests.test_examples.ExampleTests.test_top_k -v
```

To see Top K counts and buckets for a ten-number list:

```bash
python3 -m examples.top_k
```

## Files to study

| File | Focus |
| --- | --- |
| [Arrays/arrays.py](Arrays/arrays.py) | Scans, sorting, two pointers, prefix sums, in-place operations |
| [Hashing/hashing.py](Hashing/hashing.py) | Sets, counts, complement lookups, grouping, hash map design |
| [Notes.py](Notes.py) | Minimum helpers, monotonic deque, duplicate-finding variants |
| [Window exercises](tests/test_windows.py) | Check fixed-size sums against direct reference answers |
| [Arrays/arrays.txt](Arrays/arrays.txt) | Array concepts and common mistakes |
| [Hashing/hashing.txt](Hashing/hashing.txt) | Hashing concepts and common mistakes |
| [Gennotes.txt](Gennotes.txt) | Complexity and approach comparisons |
| [test.py](test.py) | Your scratch space; currently empty |
| [tests/](tests/) | Reference checks, boundary cases, and exhaustive small inputs |

Run the nearby examples with `python3 Arrays/arrays.py` or
`python3 Hashing/hashing.py`. Importing these modules keeps the examples quiet:

```python
from Hashing.hashing import top_k_frequent

print(top_k_frequent([1, 1, 2, 2, 3], 2))  # [1, 2]
```

## Deeper notes

- [Top K walkthrough](docs/top-k-walkthrough.md): list length, frequency buckets,
  tied counts, and why the stopping check belongs inside the inner loop.
- [Arrays and hashing reference](docs/practice-reference.md): function contracts,
  complexity tables, and related approaches to compare.
- [Pattern roadmap](docs/pattern-roadmap.txt): cues for later topics, including
  stacks, search, trees, graphs, and dynamic programming. This is a study guide;
  the executable exercises currently concentrate on arrays and hashing.

Some older practice functions and `Solution` classes intentionally share names.
A normal import exposes the last definition with a given name. The tests capture
each definition before it is replaced, so earlier variants are checked too.
Prefer unique names for new exercises so you can call each one directly.

Hash-based time bounds assume average table operations. Check each function's
contract: empty-input behavior and mutation rules differ between exercises.
