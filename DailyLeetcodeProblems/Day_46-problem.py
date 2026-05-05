# #Valid palindrom : 
# 125. Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def Validity():
  pass 

#step 1 use .join and .lower as well and store it in list and check if arr[i] == arr[::-1]

# arr = "mam"
# def validiy(arr):
#   for i in range(len(arr)): 
#     if arr == arr[::-1]:
#       return "It's a palindrome"

# print(validiy(arr))

# converting all the list into lower and non alphabetic 
import re 
def VALIDITYh(string):
    # string = arr.strip()
    # print(string)
    #re.sub() --> finds or seeraches and replaces the text with given condtion 
    combined = "".join(string)
    result = re.sub(r'[^a-zA-Z0-9]' , '' ,combined)
    low= result.lower()
    print(low)
    for i in range(len(low)):
      if low == low[::-1]:
        return True
      else : 
        return False


string = "0P"
print(VALIDITYh(string))

