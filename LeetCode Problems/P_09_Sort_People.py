#SOrt the People : 
class Solution(object): 
  def sortPeople(self , names , heights):
    people = zip(heights, names)
    people = sorted(people , reverse=True)
    return [name for height,name in people]
      
    
  

names = ["Mary","John","Emma"]
heights = [180,165,170]
sol = Solution() 
last = sol.sortPeople(names , heights)
print(last)