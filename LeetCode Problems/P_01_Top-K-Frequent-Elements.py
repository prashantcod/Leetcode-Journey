from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        buck = [ [] for _ in range(len(nums) + 1 )]

        for num,count in freq.items(): 
          buck[count].append(num)
    
        result = []
        for count in range(len(nums), 0, -1):  
           for num in buck[count]:
              result.append(num)
              if len(result) == k:
                 return result

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))

