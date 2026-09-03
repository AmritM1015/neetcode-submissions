class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First Attempt
        # # how do we keep track of the column?
        # # find the column first
        # col = 0
        # low = 0 
        # high = len(matrix[0]) - 1
        # for i in range(len(matrix[0])):
        #     mid = low + (high-low)//2
        #     if target < matrix[len(matrix)-1][mid]:
        #         high = mid
        #     elif target > matrix[len(matrix)-1][mid]:
        #         low = mid
        #     else:
        #         col = mid
        #         break
        # # find the row
        # row = 0
        # lptr = 0
        # rptr = len(matrix)-1
        # for i in range(len(matrix)):
        #     mid = lptr + (rptr-lptr) // 2
        #     if target < matrix[mid][col]:
        #         rptr = mid
        #     elif target > matrix[mid][col]:
        #         lptr = mid
        #     else:
        #         row = mid
        # return matrix[row][col] == target        
        m,n = len(matrix),len(matrix[0])
        r,c = 0, n-1

        while r < m and c >=0:
            if matrix[r][c] > target:
                c-=1
            elif matrix[r][c] < target:
                r+=1
            else:
                return True
        return False
