# def finding_first_index(haystack , needle): 
#   if needle == "": 
#       return 0 
#   for i in range(len(haystack) + 1 -len(needle)) : 
#      for j in range(len(needle)): 
#            if haystack[ i + j] != needle[j]: 
#                 break 
#            if j == len(needle)-1 : 
#              return i 
#   return -1 



# haystack = "sadbutsad"
# needle = "sad"
# ans = finding_first_index(haystack , needle)
# print(ans)


# ------------------------------------------------------------------------------

def finding_first_index(haystack , needle): 
  if needle == "": 
      return 0 
  for i in range(len(haystack) + 1 -len(needle)) : 
     if haystack[i : i + len(needle)] == needle : 
         return i 
  return -1 



haystack = "sadbutsad"
needle = "sad"
ans = finding_first_index(haystack , needle)
print(ans)