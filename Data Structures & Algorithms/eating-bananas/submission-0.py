class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_speed = high

        while low <= high:
            k = low + (high - low)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/k)
            if totalTime <= h:
                min_speed = k
                high = k-1
            else:
                low = k+1
        return min_speed


        # Ok so I didnt finish in 15 minutes this was my initial thoughts
        # # Ok so basically we have some piles, and we are trying to find the minimum eating speed for which we eat k bannanas maximizing bananas
        # # eaten in h hours
        # # What if we sort piles?
        # piles.sort()
        # num_piles = len(piles)
        # # The piles are in order so we can try a binary search where we choose the amount of bananas eaten as the middle of the pack,
        # # then try to calculate number of bananas eaten in the time
        # i = 0
        # low = 0
        # high = len(piles)-1
        # while True:
        #     k = low + (high + low)/2
        #     # We could just do pile//k + 1 per index and then sum up all of them for the maximum bananas eaten and then try other indices
        #     pile//k + 1 for pile in piles

            
            