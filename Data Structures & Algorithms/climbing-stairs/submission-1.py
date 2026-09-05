class Solution:
    def climbStairs(self, n: int) -> int:
        # def dfs(i):
        #     if i >=n:
        #         return i == n
        #     return dfs(i+1) + dfs(i + 2)
        # return dfs(0)
        cache = [None] * n
        def dfs(i):
            if i>=n:
                return i == n
            if not cache[i] is None:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)

