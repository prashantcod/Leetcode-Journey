# 3194. Minimum Average of Smallest and Largest Elements

def minimumAvg(nums): 
  averages = []
  nums.sort()
  i = 0 
  j = len(nums)-1
  while len(nums)//2: 
    avg = (nums[i]+ nums[j])/2
    nums.remove(nums[i])
    j = j-1 
    nums.remove(nums[j])
    j = j -1 
    averages.append(avg)
    
  return min(averages)
    
     


nums = [7,8,3,4,15,13,4,1]
ans = minimumAvg(nums)
print(ans)