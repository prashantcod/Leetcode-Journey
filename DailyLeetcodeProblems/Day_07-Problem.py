#! 961. N-Repeated Element in Size 2N Array
# Topics
# premium lock icon
# Companies
# You are given an integer array nums with the following properties:

# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

 
# Example 1:

# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:

# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:

# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5


#CODE : 
from collections import Counter 
class Solution(object):
    def repeatedNTimes(self, nums):
      counts = Counter(nums) 
      if counts: 
        mce = counts.most_common(1) #give me  1 most common/frequent element in lsit [(2) , 3)]
        return mce[0][0]
      
    
nums = [1,2,3,3]
sol = Solution() 
last = sol.repeatedNTimes(nums)
print(last)