class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Ok so first obvious approach is double for loop (Time limit exceeded from this solution)
        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j != i:
        #             res[i]*= nums[j]
        # return res
        # Ok so since the recommended time and space complexity is O(n), I would guess that we store a hashset
        # The hint mentions we could try storing solutions, this leads me to believe that its more of Dynamic Programming
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right
            right*=nums[i]
        return res