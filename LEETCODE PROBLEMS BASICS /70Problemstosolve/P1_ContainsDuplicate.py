class Solution:
    def containsDuplicate(self, nums):
        # nums.sort()
        # for i in range(1 , len(nums)):  #O(N LOG N )
        #     if nums[i] != nums[i-1]:
        #         continue 
        #     else : 
        #         return True 
        # return False
      #another method is to return --> more optimized one (O(N))
        return len(nums) != len(set(nums))

nums= [1,2,3,1]
sol = Solution() 
last = sol.containsDuplicate(nums)
print(last)


