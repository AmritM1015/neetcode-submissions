class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # We have to find 2 distinct indices in the array such that nums[i] == nums[j] and abs(i-j) <= k
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    if abs(i-j) <= k:
                        return True
        return False