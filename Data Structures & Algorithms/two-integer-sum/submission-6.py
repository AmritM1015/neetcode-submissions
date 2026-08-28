class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     complement = target-nums[i]
        #     if complement in nums:
        #         if i < nums.index(complement):
        #             return [i,nums.index(complement,i+1)]
        #         return [nums.index(complement,i+1),i]
        # return -1
        prevMap = {}

        for i,n in enumerate(nums):
            complement = target-n
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[n] = i 