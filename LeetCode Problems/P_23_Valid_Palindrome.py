#Palindrome tho ? 
import re 


def Valid_Palindrome(s): 
  s = s.lower()
  rr = re.sub(r'[^a-zA-Z0-9]','',s)
  rr=list(rr)
  j = len(rr)-1
  for i in range(len(rr)//2): 
    if rr[i] == rr[j]: 
      j -= 1 
    else : 
      return False 
  return True
      
    
    
  
   

s = "A man, a plan, a canal: Panama"
ans = Valid_Palindrome(s)
print(ans)
