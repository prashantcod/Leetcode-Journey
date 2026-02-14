# 3714. Longest Balanced Substring II


# You are given a string s consisting only of the characters 'a', 'b', and 'c'.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

 

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "aabcc"

# Output: 3

# Explanation:

# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

# Constraints:

# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.




class Solution(object):
    def longestBalanced(self, s):
        n = len(s)
        ans = 0
        
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j
        
        for x, y in (('a','b'), ('a','c'), ('b','c')):
            diff = 0
            first = {0: -1}
            start = -1
            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    diff = 0
                    first = {0: i}
                    start = i
                    continue
                diff += 1 if ch == x else -1
                if diff in first:
                    ans = max(ans, i - first[diff])
                else:
                    first[diff] = i
        
        a = b = c = 0
        first = {(0, 0): -1}
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (b - a, c - a)
            if key in first:
                ans = max(ans, i - first[key])
            else:
                first[key] = i
        
        return ans
