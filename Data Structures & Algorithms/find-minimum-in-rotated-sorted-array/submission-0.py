class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        minimum = nums[L]
        while L <= R:
            if nums[L] < nums[R]: # this would mean that this window is sorted
                minimum = min(minimum,nums[L])
                break
            mid = L + (R-L)//2
            minimum = min(nums[mid],minimum)
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
        return minimum
