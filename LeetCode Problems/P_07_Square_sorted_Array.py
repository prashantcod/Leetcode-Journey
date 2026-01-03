#! Squares of a Sorted Array

class Solution(object): 
  def sortedSquares(self,nums):
    result = [x**2 for x in nums]
    result.sort()
    return result
  

nums = [-7,-3,2,3,11]
sol = Solution()
last = sol.sortedSquares(nums)
print(last)