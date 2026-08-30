class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        resProfit = 0
        lowestBuy = prices[0]

        for i in range(1, len(prices)):
            resProfit = max(prices[i] - lowestBuy, resProfit)
            lowestBuy = min(lowestBuy, prices[i])
        
        return resProfit