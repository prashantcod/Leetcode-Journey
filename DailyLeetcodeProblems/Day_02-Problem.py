#Maximize Happiness of selected Children
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        result = 0 
        happiness.sort(reverse=True)
        for i in range(k): 
            gain = happiness[i]-i
            if gain > 0 : 
                result += gain 
            else: 
                break 
        return result

happiness = [1,2,3] 
k =2 
sol = Solution()
last = sol.maximumHappinessSum(happiness, k)
print(last)
                
            
            
                
        


        
        