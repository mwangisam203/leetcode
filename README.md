# LeetCode practice

Current files:

- [Arrays](Arrays/arrays.py): scans, sorting, two pointers, prefix sums, in-place operations, and running optima.
- [Hashing](Hashing/hashing.py): sets, frequency counting, prefix lookups, string mappings, and hash map design.
- [Array notes](Arrays/arrays.txt) and [hashing notes](Hashing/hashing.txt).
- [Additional examples](Notes.py), [scratch practice](test.py), and [summary table](Gennotes.txt).
- [Original example checks](tests/test_examples.py) and [additional pattern checks](tests/test_patterns.py).

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

=== GOLDEN NUGGETS: PATTERN RECOGNITION CHEAT SHEET ===
Purpose: when you see a problem, match its cues to a pattern FAST, before you start coding.
Format per pattern: CUES (what tips you off) -> INTUITION -> GO-TO TECHNIQUE -> COMPLEXITY

This covers the full NeetCode-style roadmap. Keep this as your "read before every session" file.

---------------------------------------------------------------------
1. ARRAYS & HASHING
---------------------------------------------------------------------
CUES: "have I seen this before", "find pair/group that sums/matches", need O(1) lookup,
      counting frequency, grouping by a derived key
INTUITION: trade space for time — store what you've seen so you never re-scan
GO-TO: dict (value->index or value->count), set (membership), Counter, defaultdict
EXAMPLES: Two Sum, Contains Duplicate, Group Anagrams, Top K Frequent, Valid Anagram
COMPLEXITY: O(1) avg per op, O(n) overall typical
WATCH FOR: "sorted array" in the prompt often signals two pointers instead is more optimal
           (still works with hashing, but two pointers can save space)


---------------------------------------------------------------------
2. TWO POINTERS
---------------------------------------------------------------------
CUES: sorted array (or can sort it), "pair that sums to X", palindrome check,
      "smaller/larger than target", merging two sequences
INTUITION: instead of checking every pair (O(n^2)), move two pointers toward each other
           (or same direction) using the sorted order to eliminate possibilities
GO-TO: left = 0, right = len(arr)-1; move based on comparison to target
EXAMPLES: Two Sum II (sorted), Valid Palindrome, 3Sum, Container With Most Water
COMPLEXITY: O(n) for a single two-pointer scan; sorting adds O(n log n).
            3Sum is O(n²); 4Sum is O(n³) with outer loops.
WATCH FOR: 3Sum/4Sum = fix one/two pointers, two-pointer the rest; always skip duplicates

---------------------------------------------------------------------
3. SLIDING WINDOW
---------------------------------------------------------------------
CUES: "substring/subarray" + "longest/shortest/contains", contiguous range,
      a window that grows/shrinks based on a condition
INTUITION: instead of recomputing every substring from scratch, expand the window's
           right edge and shrink the left edge, maintaining state incrementally
GO-TO: left, right pointers + a hash map/set/counter tracking the window's contents
EXAMPLES: Longest Substring Without Repeating Characters, Minimum Window Substring,
          Longest Repeating Character Replacement, Sliding Window Maximum (deque)
COMPLEXITY: O(n) — each pointer moves forward only, total n+n moves
WATCH FOR: "fixed size k" windows are simpler (just slide, no need to shrink dynamically);
           variable-size windows often shrink in a while-loop when the condition breaks.
           Sum-based windows need suitable constraints; negative numbers can
           invalidate greedy shrinking, so consider prefix sums instead.

---------------------------------------------------------------------
4. STACK
---------------------------------------------------------------------
CUES: matching pairs (parentheses/brackets), "next greater/smaller element",
      undo/backtrack behavior, evaluate expressions, nested structure
INTUITION: last-in-first-out mirrors nested/matching structures naturally —
           whatever you opened most recently is what you close first
GO-TO: list used as a stack (.append/.pop), sometimes stack of (value, index) pairs
EXAMPLES: Valid Parentheses, Min Stack, Evaluate RPN, Daily Temperatures (monotonic stack),
          Largest Rectangle in Histogram
COMPLEXITY: O(n) — each element pushed/popped at most once (even in monotonic stack)
WATCH FOR: "next greater element" style problems -> monotonic stack (stack stays
           increasing or decreasing; pop when the new element breaks the order)

---------------------------------------------------------------------
5. BINARY SEARCH
---------------------------------------------------------------------
CUES: sorted array, "find target in O(log n)", "find boundary/rotation point",
      search space can be framed as a range even if not an explicit array
INTUITION: repeatedly cut the search space in half using a condition that's
           monotonic (true/false doesn't flip back and forth)
GO-TO: left, right = 0, len(arr)-1; while left <= right: mid = (left+right)//2
EXAMPLES: Binary Search, Search in Rotated Sorted Array, Find Minimum in Rotated Array,
          Koko Eating Bananas (binary search on the ANSWER, not the array)
COMPLEXITY: O(log n) for array search; answer-space search costs
            O(check_cost * log(search_range)).
WATCH FOR: "binary search on the answer" — if a problem asks to minimize/maximize a value
           and you can check "is X feasible?" in O(n), binary search the value itself

---------------------------------------------------------------------
6. LINKED LIST
---------------------------------------------------------------------
CUES: node/pointer structure, "reverse", "detect cycle", "merge two lists",
      "find middle", "Nth from end"
INTUITION: no random access — everything is done by carefully moving pointers;
           many problems reduce to "fast and slow pointer" or "reverse pointers in place"
GO-TO: fast/slow (Floyd's) pointers for cycle/middle detection; dummy head node
       to simplify edge cases when building a new list
EXAMPLES: Reverse Linked List, Linked List Cycle, Merge Two Sorted Lists,
          Remove Nth Node From End, Reorder List, LRU Cache (list + hashmap)
COMPLEXITY: O(n) time, O(1) space typical (in-place pointer manipulation)
WATCH FOR: always ask "do I need a dummy node?" before writing list-building code —
           it eliminates a huge class of null-pointer edge cases

---------------------------------------------------------------------
7. TREES (BINARY TREE / BST)
---------------------------------------------------------------------
CUES: node with left/right children, "traverse", "depth/height", "path sum",
      "is it balanced/valid BST", "lowest common ancestor"
INTUITION: almost everything is recursion — solve for a node assuming its children
           are already solved (trust the recursion), then combine results
GO-TO: recursive DFS (preorder/inorder/postorder) as default; BFS with a queue
       when the problem is about LEVELS
EXAMPLES: Invert Binary Tree, Maximum Depth, Same Tree, Validate BST,
          Lowest Common Ancestor, Binary Tree Level Order Traversal, Diameter of Tree
COMPLEXITY: O(n) time (visit every node once), O(h) space for recursion stack (h = height)
WATCH FOR: BST property (left < node < right) lets you prune — don't treat every
           tree problem like a generic binary tree if it explicitly says BST

---------------------------------------------------------------------
8. TRIES
---------------------------------------------------------------------
CUES: "prefix", "autocomplete", "word search in a dictionary", many strings
      sharing common prefixes
INTUITION: a tree where each path from root spells a prefix — shared prefixes
           share nodes, so you avoid re-storing/re-scanning common beginnings
GO-TO: nested dict (children = {}) or a TrieNode class with children + is_end flag
EXAMPLES: Implement Trie, Word Search II, Design Add and Search Words
COMPLEXITY: O(m) per insert/search where m = word length (not dependent on # of words stored)
WATCH FOR: this is a less common category but shows up specifically when "prefix" is
           in the problem description — don't force it elsewhere

---------------------------------------------------------------------
9. HEAP / PRIORITY QUEUE
---------------------------------------------------------------------
CUES: "Kth largest/smallest", "top K", "merge K sorted lists", "median of a stream",
      need repeated access to min/max as data changes
INTUITION: a structure that keeps the min (or max) accessible in O(log n) insert/remove,
           instead of re-sorting every time something changes
GO-TO: Python's heapq (min-heap by default; negate values for a max-heap)
EXAMPLES: Kth Largest Element, Top K Frequent Elements (heap alternative to bucket sort),
          Merge K Sorted Lists, Find Median from Data Stream (two heaps)
COMPLEXITY: O(log n) insert/pop, O(n log k) for "top k of n" style problems
WATCH FOR: "top K" can be solved with heap OR bucket sort (see hashing notes) —
           heap is more general, bucket sort is faster when frequency range is bounded

---------------------------------------------------------------------
10. BACKTRACKING
---------------------------------------------------------------------
CUES: "all possible combinations/permutations/subsets", "generate all valid X",
      constraint satisfaction (N-Queens, Sudoku), decision tree exploration
INTUITION: try a choice, recurse, undo the choice (backtrack) if it doesn't pan out —
           explore the full decision tree but prune branches that can't work
GO-TO: recursive function with a "path so far" + choices remaining; append to path,
       recurse, then pop from path (the undo step is what makes it backtracking)
EXAMPLES: Subsets, Permutations, Combination Sum, Word Search, N-Queens
COMPLEXITY: often exponential (O(n * 2^n) for materialized subsets,
           O(n * n!) for materialized permutations) — that's expected and fine for these problems,
           the skill being tested is correct pruning, not beating exponential time
WATCH FOR: always explicitly undo state (pop/remove) after the recursive call returns —
           forgetting this is the #1 backtracking bug

---------------------------------------------------------------------
11. GRAPHS
---------------------------------------------------------------------
CUES: nodes + edges (explicit or implied, e.g. grid = graph where cells are nodes),
      "connected components", "shortest path", "can you reach X from Y",
      "islands", "course scheduling" (dependency = directed edge)
INTUITION: BFS for shortest path / level-by-level spread; DFS for exploring all
           reachability or detecting structure (cycles, connected components)
GO-TO: adjacency list (dict of lists), visited set, BFS with queue OR DFS with
       recursion/stack depending on whether "shortest" matters
EXAMPLES: Number of Islands (DFS/BFS on grid), Clone Graph, Course Schedule (cycle
          detection = topological sort), Pacific Atlantic Water Flow
COMPLEXITY: O(V + E) for BFS/DFS
WATCH FOR: "shortest path" on UNWEIGHTED graph -> BFS (not DFS); DFS does not
           guarantee shortest path. For weighted paths, use Dijkstra with nonnegative weights or an
           appropriate alternative such as Bellman-Ford (see below)

---------------------------------------------------------------------
12. ADVANCED GRAPHS
---------------------------------------------------------------------
CUES: weighted edges + "shortest/cheapest path", "minimum cost to connect all",
      negative weights mentioned
INTUITION: BFS/DFS assume equal edge cost — once edges have weights, you need
           algorithms that account for cost, not just hop count
GO-TO: Dijkstra (heap-based, non-negative weights), Bellman-Ford (handles negative
       weights), Union-Find / Kruskal's or Prim's (minimum spanning tree)
EXAMPLES: Network Delay Time (Dijkstra), Cheapest Flights Within K Stops (Bellman-Ford
          style), Min Cost to Connect All Points (MST)
COMPLEXITY: Dijkstra O(E log V) with a heap; Bellman-Ford O(V * E)
WATCH FOR: this category is less common early on — deprioritize until Trees/Graphs
           fundamentals are solid

---------------------------------------------------------------------
13. 1-D DYNAMIC PROGRAMMING
---------------------------------------------------------------------
CUES: "number of ways to...", "minimum/maximum cost to reach...", overlapping
      subproblems, decisions that build on previous decisions (climbing stairs,
      house robber style)
INTUITION: break the problem into smaller versions of itself, solve each smaller
           version ONCE, store the answer (memoize), reuse it instead of recomputing
GO-TO: define dp[i] = answer using only the first i elements; find the recurrence
       relating dp[i] to dp[i-1] (and/or dp[i-2], etc.); start bottom-up with a list,
       or top-down with recursion + a memo dict
EXAMPLES: Climbing Stairs, House Robber, Coin Change, Longest Increasing Subsequence,
          Word Break
COMPLEXITY: depends on the recurrence; e.g. O(n) for House Robber,
            O(amount * number_of_coins) for Coin Change, O(n²) for basic LIS DP
WATCH FOR: always write the recurrence relation in plain English BEFORE coding —
           "dp[i] = min(dp[i-1], dp[i-2]) + cost[i]" style. If you can't state it,
           you're not ready to code it yet.

---------------------------------------------------------------------
14. INTERVALS
---------------------------------------------------------------------
CUES: pairs of [start, end], "merge overlapping", "meeting rooms",
      "insert a new interval", scheduling
INTUITION: merging intervals typically sorts by start time; compare each
           interval with the last merged interval. For maximum non-overlapping
           intervals, a greedy solution sorts by end time instead
GO-TO: sort intervals by start; iterate, comparing current.start to prev.end
EXAMPLES: Merge Intervals, Insert Interval, Non-overlapping Intervals,
          Meeting Rooms II (often needs a heap to track end times)
COMPLEXITY: O(n log n) — dominated by the sort
WATCH FOR: "minimum rooms needed" style (Meeting Rooms II) needs a heap of end
           times, not just sorting — recognize when simple sort isn't enough

---------------------------------------------------------------------
15. GREEDY
---------------------------------------------------------------------
CUES: "maximize/minimize", local choices that seem obviously best,
      no need to reconsider past decisions
INTUITION: at each step, take the choice that looks best right now, and trust
           that a sequence of locally-best choices produces the global best —
           only works when the problem has "greedy choice property" (not all do)
GO-TO: sort first if order matters, then a single pass making the obvious choice
EXAMPLES: Maximum Subarray (Kadane's), Jump Game, Gas Station, Task Scheduler
COMPLEXITY: usually O(n) or O(n log n) if sorting first
WATCH FOR: greedy is risky — if you can't quickly justify WHY the local choice is
           always safe, the problem may actually need DP instead. When stuck between
           the two, try to find a counterexample to your greedy idea first.

---------------------------------------------------------------------
16. ADVANCED DP (2-D / MULTI-DIMENSIONAL)
---------------------------------------------------------------------
CUES: two sequences being compared (strings/arrays), grid traversal with choices,
      "edit distance", "longest common subsequence"
INTUITION: same DP idea as 1-D, but the subproblem now depends on TWO indices
           (position in sequence A, position in sequence B) instead of one
GO-TO: dp[i][j] = answer using first i of A and first j of B; 2D table,
       often can be space-optimized to two 1D rows since dp[i] only needs dp[i-1]
EXAMPLES: Longest Common Subsequence, Edit Distance, Unique Paths (grid),
          0/1 Knapsack
COMPLEXITY: O(n*m) time and space (often optimizable to O(min(n,m)) space)
WATCH FOR: draw the 2D grid on paper before coding — visualizing which cell depends
           on which neighbors makes the recurrence obvious

---------------------------------------------------------------------
17. BIT MANIPULATION
---------------------------------------------------------------------
CUES: "without using +/-", "count set bits", XOR mentioned, "single number
      among duplicates", powers of 2
INTUITION: numbers are bits underneath — XOR cancels duplicates (a^a=0),
           AND/OR/shift can replace arithmetic or check specific bit positions
GO-TO: know XOR (^), AND (&), OR (|), NOT (~), left shift (<<), right shift (>>)
EXAMPLES: Single Number (XOR all -> duplicates cancel, single value remains),
          Number of 1 Bits, Counting Bits, Missing Number (XOR trick)
COMPLEXITY: O(n) or O(log n) (log n for bit-length-dependent operations)
WATCH FOR: this category is small but has "aha or nothing" problems — if you don't
           see the bit trick quickly, you likely won't derive it under pressure,
           so pattern-memorize the handful of classic XOR tricks specifically

---------------------------------------------------------------------
CROSS-CUTTING GOLDEN RULES (apply regardless of topic)
---------------------------------------------------------------------
1. "O(1) lookup needed" anywhere in your reasoning -> reach for hash map/set,
   regardless of what topic folder the problem is filed under.
2. "Sorted" in the problem (or "can I sort it without breaking the answer?")
   -> consider two pointers or binary search before anything fancier.
3. If brute force is O(n^2) and you sense it should be faster, ask:
   - Can I precompute something once and look it up? (hashing)
   - Can I use two pointers instead of nested loops? (two pointers)
   - Can I avoid recomputation with a sliding window? (sliding window)
   - Am I solving the same subproblem repeatedly? (DP)
4. When stuck, state the brute force solution and its complexity FIRST, out loud —
   it clarifies the problem and gives the interviewer something to work with,
   and often the optimization becomes obvious once brute force is stated clearly.
5. Always confirm: time complexity, space complexity, and edge cases (empty input,
   single element, all duplicates, negative numbers) before declaring done.
