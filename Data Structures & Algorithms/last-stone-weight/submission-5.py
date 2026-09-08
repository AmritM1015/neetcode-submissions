class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We can just use Binary Search to add the stone rather than just appending it to the end of the list so we can avoid having to sort
        stones.sort()
        n = len(stones)
        while n > 1:
            # stones.sort()
            x = stones.pop()
            y = stones.pop()
            diff = abs(x-y)
            n-=2
            if diff > 0:
                l,r = 0,n
                while l < r:
                    mid = l + (r-l)//2
                    if stones[mid] < diff:
                        l = mid+1 # so basically we are trying to make l track our stopping number
                    else:
                        r = mid
                n+=1
                stones.append(0) # ig we are appending zero because we dont care about the remaining value?
                for i in range(n-1,l,-1):
                    stones[i] = stones[i-1]
                stones[l] = diff
        return stones[0] if n > 0 else 0
        
        # Sorting (requires you to sort in every iteration - not ideal)
        # while len(stones) > 1:
        #     stones.sort()
        #     x = stones.pop(-1)
        #     y = stones.pop(-1)
        #     if x != y:
        #         stones.append(abs(x-y))
        # return stones[0] if len(stones) > 0 else 0