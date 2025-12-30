#! Pyramid Transition Matrix : 
# You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

# To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

# For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
# You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

# Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

#CODE 
from typing import List
from collections import defaultdict
# this is my solution

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        trans = defaultdict(list)
        for rule in allowed:
            trans[rule[:2]].append(rule[2])

        def dfs(row):
            if len(row) == 1:
                return True
            def build_next(i, curr):
                if i == len(row) - 1:
                    return dfs(curr)

                pair = row[i:i+2]
                if pair not in trans:
                    return False

                for ch in trans[pair]:
                    if build_next(i + 1, curr + ch):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)

bottom = "BCD"
allowed = ["BCC" , "CDE" , "CEA" ,"FFF" ]
sol = Solution() 
last = sol.pyramidTransition(bottom , allowed)
print(last)













