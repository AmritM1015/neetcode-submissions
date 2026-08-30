class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        history = []
        max_profit = 0
        for i,price in enumerate(prices):
            profits = [price-i for i in history]
            maximum = 0
            if len(profits) != 0:
                maximum = max(profits)
            if maximum > max_profit:
                max_profit = maximum
            history.append(price)
        return max_profit
