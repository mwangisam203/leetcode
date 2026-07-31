def validAnagram(t, s):
    if len(t) != len(s):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count == 0:
            return False
        count[char] -= 1

    return True
print(validAnagram("jess", "jess"))

my_cart = [23, 9, 13, 6, 18, 1, 25, 2]

smallest_number = my_cart[0]

for num in my_cart:
    if num < smallest_number:
        smallest_number = num
print(smallest_number)



def minVal(myArray):

    minVal = myArray[0]

    for i in myArray:
        if i < minVal:
            minVal = i

    return minVal

            
print(minVal([100, 250, 23, 50, 0]))


class Solution:
    def findMin(self, nums):
        minimum = nums[0]

        for num in nums:
            if num < minimum:
                minimum = num
        return minimum

solution = Solution()
ans = solution.findMin([13, 3, 5, 2])