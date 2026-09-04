class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        new_list = self.nums.copy()
        new_list.sort()
        return new_list[len(new_list)-self.k]
        
