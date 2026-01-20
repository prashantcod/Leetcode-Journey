# 3315. Construct the Minimum Bitwise Array II
class Solution(): 
  def BitwiseArray(self , nums):
    ans = []
    for i in range(len(nums)):
      found = False
      for x in range(nums[i]):
          if (x | (x+1)) == nums[i]:
              ans.append(x)
              found = True
              break
      if (found == False):
            ans.append(-1)
    return ans


    
nums = [2,3,5,7]
sol = Solution()
value = sol.BitwiseArray(nums)
print(value)