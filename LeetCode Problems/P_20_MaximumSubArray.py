#MAXIMUM SUBARRRAY USING KADANE'S ALGORITHM : 

class Solution (): 
  def maxsubarray(self, nums ): 
    max_sum = 0 
    curr_sum =0 
    for i in range(len(nums)): 
      curr_sum += nums[i]
      max_sum = max(curr_sum , max_sum) 
      if (curr_sum < 0): 
         curr_sum = 0   # ignore the negative values 
    return max_sum 

nums = [-2,1,-3,4,-1,2,1,-5,4] ; 
sol = Solution()
value = sol.maxsubarray(nums)
print(value)