class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,col = len(image),len(image[0])
        # Change color of starting pixel
        orig = image[sr][sc] # color of the starting pixel
        if orig == color:
            return image 
        # All directly adjacent pixels that share the same color as the starting pixel are altered
        def dfs(r,c):
            if(min(r,c) < 0 or r >= row or c >= col or image[r][c] != orig): # if we are out of bounds and the image row and col dont share the
                return                                                       # same pixel value as the original image then exit
            image[r][c] = color                                          
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc)
        return image           
             