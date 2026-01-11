# # 85. Maximal Rectangle


# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.
 
# CODE 
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Update histogram heights
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Calculate max rectangle in histogram
            stack = []
            for k in range(cols + 1):
                curr_height = heights[k] if k < cols else 0

                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = k if not stack else k - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(k)

        return max_area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
sol = Solution()
last = sol.maximalRectangle(matrix)
print(last)