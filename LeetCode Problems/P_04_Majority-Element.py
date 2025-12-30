# MAJORITY ELEMENT : 
class Solution(object): 
  def MajorityElement(self , nums):
    nums.sort()
    return nums[len(nums)//2]


nums = [6,6,6,7,7]
sol = Solution()
last = sol.MajorityElement(nums)
print(last)