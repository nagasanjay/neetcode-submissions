class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for index in range(len(prices)):
            profit = max(profit, prices[index] - minBuy)
            minBuy = min(minBuy, prices[index])
        
        return profit