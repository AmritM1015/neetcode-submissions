class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We could try doing two pointer search where we have the lower bound and upper bound and store a max left and max right while moving to the middle since we care mostly height1xheight2 = storage_max
        max_store = 0
        lptr = 0
        rptr = len(heights)-1
        lmax,rmax = 0,0 # Lmax and Rmax store
        while lptr < rptr:
            lmax = max(heights[lptr],lmax)
            rmax = max(heights[rptr],rmax)
            cur_store = min(heights[lptr], heights[rptr]) * (rptr - lptr)
            max_store = max(max_store,cur_store)
            if heights[lptr] > heights[rptr]:
                rptr-=1
            else:
                lptr+=1
        
        return max_store
