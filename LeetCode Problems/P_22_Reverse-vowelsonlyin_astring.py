# 345. Reverse Vowels of a String

a = "IceCreAm"
s= list(a)
def reverse_string(s): 
  i= 0 
  j = len(s)-1
  vowels=set('aeiouAEIOU')
  while i < j : 
    if s[i] not in vowels: 
      i += 1 
    elif s[j] not in vowels: 
      j-= 1 
    else : 
      s[i]  , s[j] = s[j] , s[i]
      i += 1 
      j -= 1 
  return "".join(s)
    

ans = reverse_string(s)
print(ans)