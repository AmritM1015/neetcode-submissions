class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low)//2
            if target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
            else:
                return mid
        return -1

        # Recursive wont work for returning index unless you deliberately store the indices as parameters

        # mid = low + (high - low)//2

        # if nums[mid] == target:
        #     return mid
        
        # if nums[mid] > target:
        #     return self.search(nums[:mid-1],target)
        # if nums[mid] < target:
        #     return self.search(nums[mid+1:],target)
        

        