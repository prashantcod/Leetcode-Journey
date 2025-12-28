#! MISSING NUMBER (EASY)

# ?My approach
class Solution(object): 
  def missingNumber(self , nums): 
    nums.sort()
    n = len(nums)
    no = [x for x in range(n+1)]
    missing_val = set(no) - set(nums)
    return list(missing_val)[0]
    

nums = [0,1]
sol = Solution()
last = sol.missingNumber(nums)
print(last)



