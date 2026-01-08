#! 1458. Max Dot Product of Two Subsequences
# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

# Example 1:

# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# Example 2:

# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# Example 3:

# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.
 




class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        
        # dp[i][j] = max dot product using nums1[i:] and nums2[j:]
        dp = [[-10**18] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                # Option 1: take current pair
                take = nums1[i] * nums2[j]
                take += max(0, dp[i][j])
                
                # Option 2: skip nums1[i]
                skip1 = dp[i][j + 1]
                
                # Option 3: skip nums2[j]
                skip2 = dp[i + 1][j]
                
                dp[i + 1][j + 1] = max(take, skip1, skip2)
        
        return dp[n][m]

nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
sol = Solution() 
value = sol.maxDotProduct(nums1,nums2)
print(value)