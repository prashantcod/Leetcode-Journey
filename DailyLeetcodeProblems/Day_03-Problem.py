# COUNT NEGATIVE NUMBERS IN A SORTED MATRIX :
class Solution(object): 
  def countNegatives(self, grid): 
    count= 0
    for row in grid: 
      for element in row: 
         if element < 0: 
            count = count + 1 
    return count 

grid = [[3,2],[1,0]]
sol = Solution()
last = sol.countNegatives(grid)
print(last)

