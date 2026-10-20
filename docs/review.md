# Practice and review

Pick one exercise and hide its implementation. First state the input contract
and a simple correct approach. Then write the optimized version and explain
what stays true after each iteration. Use `test.py` for scratch attempts.

## Suggested next sessions

| Session | Exercise | Explain before coding | Check |
| --- | --- | --- | --- |
| 1 | Top K Frequent | Why can a tied bucket skip past k? | `tests.test_examples.ExampleTests.test_top_k` |
| 2 | Fixed-size maximum sum | What enters and leaves the sum? | `tests.test_windows` |
| 3 | Longest unique substring | Why must shrinking use a while-loop? | `tests.test_windows` |
| 4 | Binary search and lower bound | What does the exclusive right boundary mean? | `tests.test_search` |
| 5 | Valid parentheses | Why are matching counts insufficient? | `tests.test_stacks` |
| 6 | Daily temperatures | What makes the first warmer day final? | `tests.test_stacks` |
| 7 | Subarray sum and zero-sum spans | Should the table store counts or earliest indices? | `tests.test_examples.ExampleTests.test_subarray_sum`, `tests.test_patterns.PatternTests.test_longest_zero_sum` |

For example, run `python3 -m unittest tests.test_search -v` from the repository
root. The checks above exercise the reference implementations. To check your
scratch attempt, call it on the same small cases and compare results; passing
the repository suite alone does not validate an unconnected scratch solution.

The [optional study schedule](study-plan.txt) gives a longer topic sequence.
Revisit an exercise the next day, several days later, and the following week.
Move on when you can explain the invariant and reconstruct the code without
copying; adjust the pace when you discover a gap.

## Questions to answer without looking

1. For `[1, 1, 2, 2, 3]`, what are n, u, and the valid k range in this repo?
2. Why is `range(n, 0 - 1)` different from `range(n, 0, -1)`?
3. Why does `values = move_zeroes(values)` lose the reference in that variable?
4. What does `prefix[i]` include? How do you sum `[start, stop)`?
5. Why is `{0: 1}` needed for subarray counts, but `{0: -1}` for longest spans?
6. Why can a fixed-size window handle negative values safely?
7. For `lower_bound([1, 2, 2, 4], 5)`, may you index the list at the result?
8. Why must equal temperatures remain in the pending stack?
9. Why can a nested while-loop still take O(n) total time?
10. Does Python's in-place sort promise O(1) temporary space?

<details>
<summary>Check your reasoning after attempting the questions</summary>

1. n=5 elements, u=3 distinct values, integer k from 0 through 3.
2. The first is `range(n, -1)` with a positive step, empty for n>=0; the second
   counts downward from n through 1.
3. The function mutates the list and returns None, which replaces the variable's
   value. Call it first, then inspect the original list.
4. `prefix[i]` sums the first i values, excluding index i. Subtract
   `prefix[start]` from `prefix[stop]`.
5. There is one empty prefix before processing anything. For counts, remember
   its multiplicity; for lengths, remember its position just before index zero.
6. The size determines which value leaves; no assumption about sum monotonicity
   is needed. A variable-size sum window needs a separate justification.
7. No. It returns 4, the position after the last element. Check the length first.
8. The task asks for strictly warmer values; equal values do not qualify.
9. Each index may enter and leave a structure at most once overall, even when
   several removals happen during one outer iteration.
10. No. It changes the original list but can use O(n) sorting workspace.

</details>

## Record a useful mistake

Copy this template into your own notes after a practice attempt:

```text
Exercise and date:
Input constraints and expected return:
My approach and invariant:
Smallest input that exposed my mistake:
Expected result / actual result:
Cause (explain the state or boundary that was wrong):
Correction and why it works:
Time / extra space / mutation:
Next review:
```

Try shrinking a failing input before changing the algorithm. A two-item tied
bucket can explain a stopping bug more clearly than a fifty-item random list.
For unordered answers compare membership or frequencies; for in-place exercises
inspect the changed list; for invalid input check the promised exception.
