"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_list = {}
        if not node:
            return None
        adj_list[node] = Node(node.val)  

        q= deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in adj_list:
                    adj_list[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                adj_list[cur].neighbors.append(adj_list[neighbor])
        return adj_list[node]
    

        
        