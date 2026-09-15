class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def coinFit(amount_left: int) -> int:
            if amount_left == 0:
                return 0

            if amount_left < 0:
                return float("inf")

            if amount_left in mem:
                return mem[amount_left]

            fewest_coins = float("inf")

            for coin in coins:
                candidate = 1 + coinFit(amount_left - coin)
                fewest_coins = min(fewest_coins, candidate)

            mem[amount_left] = fewest_coins
            return fewest_coins

        result = coinFit(amount)

        return -1 if result == float("inf") else result