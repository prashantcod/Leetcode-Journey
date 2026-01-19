def twoSum( nums , target):
    hashmap = {}
    for i ,v  in enumerate(nums):
      diff = target - v
      if diff in hashmap:
        return [i , hashmap[diff]]
      else : 
        hashmap[v] = i 
    
nums=[2,7,11,15]
target = 9
sol = twoSum(nums , target)
print(sol)
