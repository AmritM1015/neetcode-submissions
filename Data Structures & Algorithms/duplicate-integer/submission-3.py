class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # d = {} 
        # for i in nums:
        #     if i not in d:
        #         d[i] = i
        #     else:
        #         return True
        # return False
        s = set()
        for i in nums:
            s.add(i)

        return len(nums) != len(s)

        # return len(nums) != len(set(nums))