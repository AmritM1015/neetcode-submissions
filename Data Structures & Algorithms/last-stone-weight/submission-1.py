class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop(-1)
            y = stones.pop(-1)
            if x != y:
                stones.append(abs(x-y))
        return stones[0] if len(stones) > 0 else 0