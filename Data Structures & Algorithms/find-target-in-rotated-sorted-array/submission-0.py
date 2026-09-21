class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Bucket 1 [3,4,5,6]
        # Bucket 2 [1,2]

        # Bucket 1 [3,5,6]
        # Bucket 2 [0,1,2]

        L = 0
        R = len(nums)-1

        while L < R:
            mid = L + (R-L)//2
            if nums[mid] > nums[R]:
                L = mid+1
            else:
                R = mid
        pivot = L

        def binary_search(left, right) -> int:
            while left <= right:
                m = left + (right-left)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1
        
        # See if Bucket 1 contains the answer 
        result = binary_search(0, pivot-1)
        if result != -1:
            return result
        
        # See if Bucket 2 contains the answer
        return binary_search(pivot, len(nums)-1)
            