
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
print(ans)



class Answer:

    def largest(self, digits: list[int]) -> int:

        largest  = digits[0]

        for large in digits:
            if large > largest:
                largest = large
        return largest

solve = Answer()
Ans = solve.largest([12, 8, 5, 50])
print(Ans)

Solution().maximum([8,4,10,2])