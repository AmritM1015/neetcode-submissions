class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # history = []
        # max_profit = 0
        # for i,price in enumerate(prices):
        #     profits = [price-i for i in history]
        #     maximum = 0
        #     if len(profits) != 0:
        #         maximum = max(profits)
        #     if maximum > max_profit:
        #         max_profit = maximum
        #     history.append(price)
        # return max_profit
        # l = 0 # buy day
        # r = 1 # sell day
        # maxP = 0
        # for i in range(len(prices)-1):
        #     if(prices[l] < prices[r]):
        #         if prices[r] - prices[l] > maxP:
        #             maxP = prices[r] - prices[l]
        #     else:
        #         l = r
        #     r+=1
        # return maxP
        minBuy = prices[0]
        maxP = 0
        for i in prices:
            if maxP < i-minBuy:
                maxP = i - minBuy
            if(minBuy > i):
                minBuy = i
        return maxP
                

