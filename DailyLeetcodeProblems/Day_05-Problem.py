# #Magic Squares in Grid : 
# A  3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there
class Solution(object):
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):

                # Center must be 5
                if grid[i+1][j+1] != 5:
                    continue

                nums = []
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        nums.append(grid[r][c])

                # Must contain numbers 1 to 9 exactly once
                if set(nums) != set(range(1, 10)):
                    continue

                # Check all sums
                if (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] == 15 and
                    grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == 15 and
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == 15 and

                    grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 and
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15 and
                    grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == 15 and

                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == 15
                ):
                    count += 1

        return count






grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
sol = Solution() 
last = sol.numMagicSquaresInside(grid)
print(last)
















