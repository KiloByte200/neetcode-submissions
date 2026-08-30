class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        memo = {} # key  -> stair: value -> min cost from stair to end


        def backtrack(stair: int) -> int:
            if stair >= n:
                return 0

            if stair in memo:
                return memo[stair]

            
            memo[stair] = cost[stair] + min(backtrack(stair + 1), backtrack(stair + 2))
            
            return memo[stair]
        
        return min(backtrack(0), backtrack(1))
        