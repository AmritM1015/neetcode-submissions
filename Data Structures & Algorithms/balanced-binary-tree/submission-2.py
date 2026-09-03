# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True,0]
            left,right = dfs(node.left),dfs(node.right)
            leftBalanced, rightBalanced = left[0], right[0]
            leftHeight,rightHeight = left[1],right[1]
            balanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

        