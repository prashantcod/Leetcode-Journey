#Concatenation of Array : 

class Solution(object): 
  def getConcatenation(self, nums): 
    return nums + nums 


nums = [1,2,1]
sol = Solution()
last = sol.getConcatenation(nums)
print(last)