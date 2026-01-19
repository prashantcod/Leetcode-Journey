# Find all the missing numbers : 
# def FMN(nums):
  # no = list(set(nums))
  # result = []
  # for i ,v  in enumerate(no): 
  #   if (i+1) != v: 
  #     result.append(v-2)
  #   if v == len(no):
  #     result.append(v+1)
  # return result

def Optimized_One(nums): 
  for i in range(len(nums)):
    temp = abs(nums[i])-1
    if nums[temp]>0:
      nums[temp] *= -1 
  
  res = []
  for i ,n in enumerate(nums):
    if n>0: 
      res.append(i+1)
  
  return res


nums = [4,3,2,7,8,2,3,1]
# last = FMN(nums)
last = Optimized_One(nums)
print(last)