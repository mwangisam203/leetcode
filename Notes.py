#What you need to know cold

#Frequency counting with Counter or a manual dict
#Checking for duplicates using a set
#Using a dict to store "value → index" so you can look things up instantly instead of re-scanning
#Sorting when order doesn't matter but grouping does (e.g., anagrams)
#Basic array traversal and prefix/suffix accumulation (running totals as you loop)

numbers = [20, 45, 87, 12, 49, 25, 0, 13]

smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num
print("smallest number is: ", smallest_number)
        
