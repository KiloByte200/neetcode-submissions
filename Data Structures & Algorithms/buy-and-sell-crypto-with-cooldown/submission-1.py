class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        memo = {}

        def priceMatch(index:int, neetcoin_held: bool) -> int:
            if index >= n:
                return 0

            if (index, neetcoin_held) in memo:
                return memo[(index, neetcoin_held)]

            best_result = 0
            # buy if neetcoin not held
            if not neetcoin_held:
                best_result = priceMatch(index+1, True) - prices[index]

            # sell if neetcoin held and skip day
            if neetcoin_held:
                best_result = max(best_result, priceMatch(index+2, False) + prices[index])

            # skip day
            best_result = max(best_result, priceMatch(index+1, neetcoin_held))

            memo[(index, neetcoin_held)] = best_result
            return memo[(index, neetcoin_held)]
        
        return priceMatch(0, False)
        