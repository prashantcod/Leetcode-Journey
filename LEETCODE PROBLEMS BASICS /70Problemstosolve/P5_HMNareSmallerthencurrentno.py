#! HOW MANY NUMBERS ARE SMALLER THAN CURRENT NUMBER 
def MininumNOarray(nums):
  temp = sorted(nums)
  d = {}
  for i , v in enumerate(temp):
    if v not in d:
      d[v] = i 
  result = []
  for i in nums: 
    result.append(d[i])
  return result
      
nums = [8,1,2,2,3]
value = MininumNOarray(nums)
print(value)
