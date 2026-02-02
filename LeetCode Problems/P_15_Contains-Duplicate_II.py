# Contains Duplicate- II : 
# Easy 

class Solution(): 
  def Contains_Duplicate(self ,nums , k):
    win = set()
    L = 0 
    for R in range(len(nums)):
      if R -L > k : 
        win.remove(nums[L])
        L = L +1 
      if nums[R] in win: 
        return True 
      win.add(nums[R])
    return False
        
      
    
              






# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
# nums = [1,2,3,1,2,3]
# k = 2

nums = [1,5,1,0] 
k =2 

sol = Solution()
value = sol.Contains_Duplicate(nums,k)
print(value)