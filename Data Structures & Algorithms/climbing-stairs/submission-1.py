class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def backtrack(stair: int) -> int:
            if stair > n:
                return 0
            
            if stair == n:
                return 1

            if stair in memo:
                return memo[stair]

            memo[stair] = backtrack(stair + 1) + backtrack(stair + 2)

            return memo[stair]
        
        return backtrack(0)
        