class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0 # we dont keep track of the locations of fresh just the amount of fresh fruit
        time = 0

        #immediately initialize the queue with all the locations of the rotten fruit
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    q.append((row,col))
            
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        while fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr, c + dc
                    if (row in range(len(grid))) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1
    




        # So clearly we are using DFS here ( I was wrong its a BFS problem)
        # We traverse through the grid, and we search for where there's a 2 value
        # If there is a 2 value, we recurse up down left and right checking for fresh fruit, and if its fresh(1) then we turn it rotten
        # R = len(grid)
        # C = len(grid[0])
        # def dfs(row,col,isSpoiled): # We keep track of a variable isSpoiled where this value is
        #     value =  grid[row,col]
        #     if value == 0:
        #         return 0
        #     else if value == 1 and isSpoiled:
        #     if value == 2:
        #         dfs
        # while row 