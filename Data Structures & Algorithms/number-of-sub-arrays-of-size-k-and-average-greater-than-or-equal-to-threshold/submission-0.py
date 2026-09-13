class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1]) # Non-inclusive 0 - k-1

        # The solution you could say is essentially a "two pointer" solution (we only keep track of one and add k)
        # We kinda only need one pointer cuz we can calculate R
        for L in range(len(arr)-k+1):
            curSum+= arr[L + k - 1] # We add to the sum starting from k-1 and increments as L increases 
            if curSum/k >= threshold:
                res+=1
            curSum -= arr[L] # We remove the leftmost pointer from the window
        return res