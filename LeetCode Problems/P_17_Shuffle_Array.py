# SHUFFLE ARRAY : 
  
def shufflearr( nums , n): 
  y = n 
  res = []
  for i in range(len(nums)): 
    if (i < y and y<len(nums)): 
      res.append(nums[i])
      res.append(nums[y])
      y += 1 
  return res




nums = [2,5,1,3,4,7]
n = 3
value = shufflearr(nums , n)
print(value)