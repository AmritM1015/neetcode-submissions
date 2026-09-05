class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n,res = len(nums), nums[0]

        # The brute force solution involves keeping a track of results and keeping track of an inner sum and comparing it to result
        # such that res will always get updated with the larger number until we reach the maximum sum that can be achieved from i to n.
        # The important part is we are looking for a contiguous array rather than the max value subset that can be created.
        # Brute Force Solution
        # for i in range(n):
        #     cur = 0
        #     for j in range(i,n):
        #         cur += nums[j]
        #         res = max(res, cur)
        # return res
        cache = {}
        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else float("-inf")
            if (i, flag) in cache:
                return cache[(i,flag)]
            if flag:
                cache[(i,flag)] = max(0, nums[i] + dfs(i+1, True))
            else:
                cache[(i,flag)] = max(dfs(i+1, False), nums[i] + dfs(i+1, True))
            return cache[(i,flag)]
        return dfs(0, False)
            

        