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
        # if len(nums) == 0:
        #     return 0
        # s = list(set(nums))
        # s.sort()
        # streaks = []
        # streak = 1
        # for i in range(len(s)-1):
        #     if(s[i] + 1 != s[i+1]):
        #         streaks.append(streak)
        #         streak=1
        #     else:
        #         streak+=1
        # streaks.append(streak)
        # return max(streaks)
        
        # Hashset is inefficient
        # numSet = set(nums)
        # longest = 0

        # for num in numSet:
        #     length = 1
        #     while (num + length) in numSet:
        #         length+=1
        #     longest = max(length,longest)
        # return longest

        mp = defaultdict(int) # stores sequence lengths at boundary positions
        res = 0 # Stores the largest sequence found
        for num in nums:
            if not mp[num]:
                length = mp[num-1] + mp[num+1] + 1
                mp[num] = length
                mp[num - mp[num-1]] = mp[num]
                mp[num+mp[num+1]] = mp[num]
                res = max(res,mp[num])
        return res
