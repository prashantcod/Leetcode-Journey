#! Richest Customer Wealth : 

class Solution(object): 
  def Richest_customer(self ,accounts): 
    sumrow = [sum(row) for row in accounts]
    return max(sumrow)
    


accounts = [[1,2,3],[3,2,1]]
sol = Solution()
last = sol.Richest_customer(accounts)
print(last)