class Solution:
    def rob(self, nums: List[int]) -> int:
        # So basically we can only do every other house: n + 2
        # We are looking for the maximum amount of money you can rob, so look at both odds and evens and compare max
        # evens = sum(nums[i] for i in range(0,len(nums)-1,2))
        # odds = sum(nums[i] for i in range(1,len(nums)-1,2))
        # This strategy doesnt work because there is also an option of skipping 2 houses rather than just one

        # So we can store paths but this solution would scale too high
        
        # We can use some kind of backtracking where we have an inner function comparing the value of skipping one house vs 2 and returns the max
        # Solution is of course inefficient due to lots of recursion needed
        # n = len(nums)
        # def findPath(index):
        #     if not index < n:
        #         return 0
        #     val = nums[index] # So we have the value, we have to add it to the return value (idk how)
        #     # I was really close in my solution to the recursive solution I put val in the wrong place
        #     # return val + max(findPath(index+1,nums),findPath(index+2,nums)) # WRONG
        #     return max(findPath(index+1),val+findPath(index+2))
        # return findPath(0)

        # # For the DP solution we should save subproblems ( Top - Down memoization)
        # n = len(nums)
        # memo = [-1] * len(nums)
        # def findPath(index):
        #     if not index < n:
        #         return 0
        #     val = nums[index] 
        #     if memo[index] != -1:
        #         return memo[index]
        #     memo[index] = max(findPath(index+1),val+findPath(index+2)) 
        #     return memo[index]
        # return findPath(0)

        # Why do it Top Down? Why not do it Bottom-Up

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]
