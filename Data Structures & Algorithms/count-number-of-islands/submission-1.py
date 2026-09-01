class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols = len(grid), len(grid[0])
        islands = 0

        # def dfs(r,c):
        #     if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == "0": # if we are out of bounds or hit another zero then we exit
        #         return
            
        #     grid[r][c] = "0" # mark as visited
        #     for drow,dcol in dirs:
        #         dfs(r+drow, c+dcol) # We use recursion to travel to adjacent squares in every direction
            
        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for drow,dcol in dirs:
                    new_row,new_col = row+drow,col+dcol
                    if min(new_row,new_col) < 0 or new_row >= rows or new_col >= cols or grid[new_row][new_col] == "0":
                        continue
                    q.append((new_row,new_col))
                    grid[new_row][new_col] = "0"
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c) # So for every island we find, the adjacent squares are set as visted and so the whole island counts as 1
                    islands+=1
        return islands


    
