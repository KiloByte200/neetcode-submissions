class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)

        def dp(i: int, holding: bool) -> int:
            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + dp(i + 2, False)
                skip = dp(i + 1, True)
                memo[(i, holding)] = max(sell, skip)

            else:
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)
                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dp(0, False)