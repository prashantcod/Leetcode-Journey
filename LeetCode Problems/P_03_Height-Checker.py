# HEIGHT CHECKER(EASY)
class Solution(object): 
  def heightChecker(self, heights): 
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)): 
      if heights[i] != expected[i]:
         count = count+1
    return count


heights = [1,1,4,2,1,3]
sol = Solution()
last = sol.heightChecker(heights)
print(last)