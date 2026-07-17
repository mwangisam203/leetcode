#What you need to know cold

#Frequency counting with Counter or a manual dict
#Checking for duplicates using a set
#Using a dict to store "value → index" so you can look things up instantly instead of re-scanning
#Sorting when order doesn't matter but grouping does (e.g., anagrams)
#Basic array traversal and prefix/suffix accumulation (running totals as you loop)

'''
| Input (n) | O(1) | O(log n) |      O(n) |  O(n log n) |             O(n²) |
| --------: | ---: | -------: | --------: | ----------: | ----------------: |
|        10 |    1 |       ~3 |        10 |         ~33 |               100 |
|       100 |    1 |       ~7 |       100 |        ~664 |            10,000 |
|     1,000 |    1 |      ~10 |     1,000 |      ~9,966 |         1,000,000 |
| 1,000,000 |    1 |      ~20 | 1,000,000 | ~19,931,000 | 1,000,000,000,000 |
'''
