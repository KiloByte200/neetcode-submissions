class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        mem = [[-1] * (amount+1) for _ in range(n)] # key -> (amount left, index in coins) value -> num of possible comb

        def uniqueChange(amount_left: int, index: int) -> int:
            if amount_left == 0:
                return 1

            if index >= n or amount_left < 0:
                return 0

            if mem[index][amount_left] != -1:
                return mem[index][amount_left]

            # keep subtracting current count
            keep = uniqueChange(amount_left - coins[index], index)
            # skip to next coin
            skip = uniqueChange(amount_left, index+1)

            mem[index][amount_left] = keep + skip

            return mem[index][amount_left]
        
        return uniqueChange(amount, 0)
        