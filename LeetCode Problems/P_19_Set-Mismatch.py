# Set-Mismatch

class Solution(): 
  def setMismatch(self , nums): 
        dup = -1 
        miss = -1 
        for i in range(len(nums)):
            if (nums[abs(nums[i])-1]<0 ): 
                dup = abs(nums[i])
            else : #make it negative 
                 nums[abs(nums[i])-1] *= -1 
        for i in range(len(nums)): 
            if (nums[i] > 0): #for positive no 
                 miss = i+1 
                 break 
        return [dup , miss]
nums = [1,2,2,4]
# nums = [1,1]
# nums = [3,2,2]
# nums = [3,2,3,4,6,5]
sol = Solution() 
value = sol.setMismatch(nums)
print(value)
       