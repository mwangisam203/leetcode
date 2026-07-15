#What you need to know cold

#Frequency counting with Counter or a manual dict
#Checking for duplicates using a set
#Using a dict to store "value → index" so you can look things up instantly instead of re-scanning
#Sorting when order doesn't matter but grouping does (e.g., anagrams)
#Basic array traversal and prefix/suffix accumulation (running totals as you loop)

my_array = [12, 14, 7, 20, 9, 3, 34, 0]

minArray = my_array[0]

for i in my_array:

    if i < minArray:
        minArray = i
print("my small number:", minArray)
