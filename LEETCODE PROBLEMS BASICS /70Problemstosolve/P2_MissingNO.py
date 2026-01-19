def MissingNUM(nums): 
   return sum(range(len(nums)+1)) -sum(nums) #optimized one O(N)
  # for i , v in enumerate(nums):   #O(N log N)
  #   if i != v : 
  #     return v-1 
  #   if v == len(nums)-1: 
  #     return v+1

nums = [3,0,1]
last = MissingNUM(nums)
print(last)