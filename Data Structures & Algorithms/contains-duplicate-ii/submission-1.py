class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # We have to find 2 distinct indices in the array such that nums[i] == nums[j] and abs(i-j) <= k
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             if abs(i-j) <= k:
        #                 return True
        # return False

        # We can optimize this by using a Hashtable and we store the key as nums[i] and the val as
        res = {}
        # ok so we store values in the hashtable we can do k-i but the in operator wo
        for i in range(len(nums)):
            if nums[i] in res and abs(i-res[nums[i]]) <= k:
                return True
            res[nums[i]] = i
        return False
             