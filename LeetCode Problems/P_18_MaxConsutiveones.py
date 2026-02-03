#Max Consecutive Ones : 

def consecutiveone(nums): 
        max_count = 0 
        counting = 0 
        for i in range(len(nums)): 
            if (nums[i] == 1 ): 
                counting += 1 
                max_count = max(max_count , counting)
            else : 
                counting = 0 
        return max_count


nums = [1, 1 ,0 ,1,1,1]
value = consecutiveone(nums)
print(value)