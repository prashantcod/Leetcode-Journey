#! Kids with the greatest no of candies : 
class Solution(object):
  def kidsWithCandies(self , candies , extracandies):
    result = []
    #maxium candy 
    max_num = candies[0]
    for i in range(len(candies)): 
          if candies[i]>=max_num:
             max_num = candies[i]
    
    for i in range(len(candies)):
      newcan = candies[i]+extracandies
      if newcan >= max_num:
        result.append(True)
      else : 
        result.append(False)
    return result
      
    
    

candies = [2,3,5,1,3]
extracandies = 3
sol = Solution()
value = sol.kidsWithCandies(candies ,extracandies)
print(value)







