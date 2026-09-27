from collections import defaultdict

def groupanagram(strs):
     res = defaultdict(list)


     for str in strs:
        count = [0] * 26

        for s in str:
            count[ord(s) - ord("a")] += 1
        res[tuple(count)].append(str)
        
        
        

