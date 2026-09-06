class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        res = []
        for i in range(len(nums)):
            freq[nums[i]]-=1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                freq[nums[j]] -= 1 # We decrease the count of j specifically in this inner loop because we're matching each j to i and seeing
                if j-1 > i and nums[j] == nums[j-1]: # if a complement exists to pair with i and j for each j choice
                    continue
                target = -(nums[i] + nums[j]) # Naturally we find the complement of the addition of the other two numbers
                if freq[target] > 0: # lookup in a dictionary is constant time so we remove the extra n loop from brute force
                    res.append([nums[i],nums[j],target])
                
            for j in range(i+1, len(nums)):
                freq[nums[j]] +=1
        return res


        # Initial attempt at brute forcing a solution: O(n^3)
        # nums.sort()
        # results = []
        # indices = []
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         for k in range (j,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 if i != j and j!=k and i != k and [nums[i],nums[j],nums[k]] not in results:
        #                     results.append([nums[i],nums[j],nums[k]])
        #                 # nums.pop(i)
        #                 # nums.pop(j)
        #                 # nums.pop(k)
        #                     indices.extend([i,j,k])     
        # return results