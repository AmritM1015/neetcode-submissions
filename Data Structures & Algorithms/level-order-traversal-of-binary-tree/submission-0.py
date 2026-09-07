# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We can probably have a inner function which returns the node and depth or adds it to a global dictionary and then create another nested
        # List storing the different levels
        res = [] # res[d] stores all the nodes at depth d
        def dfs(node,depth): # Output: int, int
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root,0)
        return res

