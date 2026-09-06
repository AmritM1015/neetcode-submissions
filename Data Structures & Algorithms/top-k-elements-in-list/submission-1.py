class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0) # already adding the values
        arr = [] # we're just basically putting it back into an array so we can sort
        for num,freq in count.items():
            arr.append([num,freq])
        arr.sort(key = lambda pair: pair[1])

        res = []
        while len(res) < k:
            res.append(arr.pop()[0])
        return res

        # initial thoughts
        # freq = {}
        # k_most = [] # ok so basically we have this k most array, we sort this array based on the frequency of the elements
        # # I presume there's some way you can sort the values and
        # for num in nums:
        #     if num not in freq:
        #         freq[num] = 1
        #     else:
        #         freq[num]+=1 
        # for key,value in freq:
        #     if k_most == []:
        #         k_most = [[key,value]]
        #     else:
        #         while k_most[
                
        