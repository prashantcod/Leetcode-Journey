#! Running Sum of 1d Array
class Solution(object): 
  def runningsum(self , nums): 
    result = []
    result.append(nums[0])
    for i  in range(1 ,len(nums)): 
      result.append(result[i-1]+nums[i])
    
    return result  
      
    

nums = [1,2,3,4]
sol = Solution()
last = sol.runningsum(nums)
print(last)