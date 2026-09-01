class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        # Change color of starting pixel
        orig = image[sr][sc] # color of the starting pixel
        if orig == color:
            return image 
        # All directly adjacent pixels that share the same color as the starting pixel are altered
        # def dfs(r,c):
        #     if(min(r,c) < 0 or r >= row or c >= col or image[r][c] != orig): # if we are out of bounds and the image row and col dont share the
        #         return                                                       # same pixel value as the original image then exit
        #     image[r][c] = color                                          
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        
        # dfs(sr,sc)
        q = deque([(sr,sc)])
        image[sr][sc] = color
        dirs = [(1,0),(-1,0),(0,1),(0,-1)] #Manual right left up down
        while q:
            r,c = q.popleft()
            for drow,dcol in dirs:
                new_row = r + drow
                new_col = c + dcol
                if min(new_row,new_col) >=0 and new_row < row and new_col < col and image[new_row][new_col] == orig:
                    image[new_row][new_col] = color
                    q.append((new_row,new_col))

        return image           
             