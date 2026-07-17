#What you need to know cold

#Frequency counting with Counter or a manual dict
#Checking for duplicates using a set
#Using a dict to store "value → index" so you can look things up instantly instead of re-scanning
#Sorting when order doesn't matter but grouping does (e.g., anagrams)
#Basic array traversal and prefix/suffix accumulation (running totals as you loop)

def hasduplicates(words):
    viewed = set()

    for word in words:
        if word in viewed:
            return True
        viewed.add(word)

    return False

print(hasduplicates(["abc", "dsc", "kqq"]))


def containDups(nums):
    seen = []

    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

print(containDups([1, 4, 7, 90, 1, 5]))
