class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {} # key -> position on board tuple -? value -> number of possible paths


        def move(row, col) -> int:
            if row == m-1 and col == n - 1:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            
            numPaths = 0

            # try move down
            if row + 1 < m:
                numPaths += move(row + 1, col)
            
            if col + 1 < n:
                numPaths += move(row, col + 1)
            
            memo[(row, col)] = numPaths

            return memo[(row, col)]
        
        return move(0, 0)

        