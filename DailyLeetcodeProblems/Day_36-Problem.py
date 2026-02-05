# 3379 : Transformed Array : easy 

# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.

# Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

# CODE 
class Solution(): 
  def transformedArray(self , nums): 
    size = len(nums)
    result = []
    for i in range(len(nums)): 
      if (nums[i] > 0): 
        n_id = (i+nums[i])%size   #right shift nums[i]
        result.append(nums[n_id])
      if (nums[i]< 0): 
        n_id = (i-abs(nums[i])+size)%size 
        result.append(nums[n_id])
      if (nums[i] == 0): 
        result.append(nums[i])
    return result 



nums = [3,-2,1,1]
# nums = [-1,4,-1]
sol = Solution() 
value = sol.transformedArray(nums)
print(value)