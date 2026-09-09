class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Ok so because this has to be O(n) that means we should avoid sorting.
        # Brute force - Inefficient O(n^2)
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak,curr = 0,num
        #     while curr in store:
        #         streak+=1
        #         curr+=1
        #     res = max(res,streak)
        # return res
        # Sorting solution - nlogn
        if len(nums) == 0:
            return 0
        s = list(set(nums))
        s.sort()
        streaks = []
        streak = 1
        for i in range(len(s)-1):
            if(s[i] + 1 != s[i+1]):
                streaks.append(streak)
                streak=1
            else:
                streak+=1
        streaks.append(streak)
        return max(streaks)
        