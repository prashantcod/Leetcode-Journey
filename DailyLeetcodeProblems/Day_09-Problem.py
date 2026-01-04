#! 1390. Four Divisors
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 0

# Code
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fourDivisorSum(n):
            factors = []
            d = 2
            
            while d * d <= n:
                if n % d == 0:
                    factors.append(d)
                    if d != n // d:
                        factors.append(n // d)
                    if len(factors) > 2:
                        return 0
                d += 1
            
            # Exactly two non-trivial divisors → total 4 divisors
            if len(factors) == 2:
                return 1 + factors[0] + factors[1] + n
            
            return 0
        
        return sum(fourDivisorSum(n) for n in nums)
        



nums = [21,4,7]
sol = Solution() 
last = sol.sumFourDivisors(nums)
print(last)