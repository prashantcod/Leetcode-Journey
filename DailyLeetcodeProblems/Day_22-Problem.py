#! Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105

# CODE 

class Solution(object):
    def maxSideLength(self, mat, threshold):
      rows, cols = len(mat), len(mat[0])

        # Step 1: Build prefix sum matrix
      prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

      for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )

        # Helper function to check square of size k
      def canMake(k):
            for i in range(rows - k + 1):
                for j in range(cols - k + 1):
                    total = (
                        prefix[i+k][j+k]
                        - prefix[i][j+k]
                        - prefix[i+k][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        # Step 3: Binary Search
      left, right = 0, min(rows, cols)
      ans = 0

      while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

      return ans




mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
threshold = 1
sol = Solution()
value = sol.maxSideLength(mat,threshold)
print(value)