from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)

    #res = defaultdict(list)

    for s in strs:
            # counting freq of each string
        Count = [0] * 26
            
        for char in s: 
            Count[ord(char) - ord('a')] += 1
        res[tuple(Count)].append(s)
    return list(res.values())


print(groupAnagram(["act","pots","tops","cat","stop","hat"]))




# res = defaultdict(list)

#         for s in strs:
#             # counting freq of each string
#             Count = [0] * 26
            
#             for char in s: 
#                 Count[ord(char) - ord('a')] += 1
#             res[tuple(Count)].append(s)
#         return list(res.values())