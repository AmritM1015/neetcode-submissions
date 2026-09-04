class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        
        # leftChild of i = heap[2 * i]
        # rightChild of i = heap[(2 * i) + 1] 
        # parent of i = heap[i // 2]
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # Initial Attempt
        # self.nums.append(val)
        # new_list = self.nums.copy()
        # new_list.sort()
        # return new_list[len(new_list)-self.k]
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
            

        
