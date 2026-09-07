# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We are processing by each level, and BFS prioritizes exploration so it traverses every level completely
        res = []
        
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

        # DFS solution (is not efficient because we repeatedly recurse through the same levels)
        # We can probably have a inner function which returns the node and depth or adds it to a global dictionary and then create another nested
        # List storing the different levels
        # res = [] # res[d] stores all the nodes at depth d
        # def dfs(node,depth): # Output: int, int
        #     if not node:
        #         return
        #     if len(res) == depth:
        #         res.append([])
        #     res[depth].append(node.val)
        #     dfs(node.left, depth+1)
        #     dfs(node.right, depth+1)
        # dfs(root,0)
        # return res


