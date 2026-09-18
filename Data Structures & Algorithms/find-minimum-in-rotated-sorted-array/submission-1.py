class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        # minimum = nums[L]
        while L < R:
            # if nums[L] < nums[R]: # this would mean that this window is sorted
            #     minimum = min(minimum,nums[L])
            #     break
            mid = L + (R-L)//2
            if nums[mid] < nums[R]: # comparing with the right bound is important, we are trying to make it so that the lower bound contains the min
                R = mid
            else:
                L = mid + 1
        return nums[L]
