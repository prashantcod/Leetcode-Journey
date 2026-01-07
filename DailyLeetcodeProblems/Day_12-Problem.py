#! 1339. Maximum Product of Splitted Binary Tree


# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104


# CODE : 
# Definition for a binary tree node.
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def TotalSum(self, root):
        if root is None:
            return 0
        return root.val + self.TotalSum(root.left) + self.TotalSum(root.right)

    def maxProduct(self, root):
        if root is None:
            return 0

        self.maxP = 0
        self.SUM = self.TotalSum(root)

        self.find(root)
        return self.maxP % (10**9 + 7)

    def find(self, root):
        if root is None:
            return 0

        leftSum = self.find(root.left)
        rightSum = self.find(root.right)

        S1 = root.val + leftSum + rightSum
        S2 = self.SUM - S1

        self.maxP = max(self.maxP, S1 * S2)
        return S1


def buildTree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root



arr = [1, 2, 3, 4, 5, 6]
root = buildTree(arr)

sol = Solution()
print(sol.maxProduct(root))
