#Happy Number
def isHappy( n):
        """
        :type n: int
        :rtype: bool
        """
        arr = list(map(int , str( n)))
        while True : 
            res = sum(_ **2 for _ in arr)
            if  res == 1 : 
                return True
            if  res == 4 :  # 4 is unhappy loop checker 
                return False
            arr = list(map(int , str(res)))
            
n = 19
he = isHappy(n)
print(he)

      
    
  

