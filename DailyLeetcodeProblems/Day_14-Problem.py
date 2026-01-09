#!865. Smallest Subtree with all the Deepest Nodes


# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
# Example 2:

# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
# Example 3:

# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

# Constraints:

# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.






from collections import deque

# ---------------- Tree Node Definition ----------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0, None

            ld, lnode = dfs(node.left)
            rd, rnode = dfs(node.right)

            if ld > rd:
                return ld + 1, lnode
            if rd > ld:
                return rd + 1, rnode


            return ld + 1, node

        return dfs(root)[1]



def build_tree(values):

    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)


    while result and result[-1] is None:
        result.pop()

    return result



if __name__ == "__main__":
    # Example 1
    root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    root = build_tree(root_list)

    sol = Solution()
    result = sol.subtreeWithAllDeepest(root)

    print(tree_to_list(result))  # Expected output: [2, 7, 4]



