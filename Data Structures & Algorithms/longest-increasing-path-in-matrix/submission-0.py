class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])

        directions = {
            (1, 0), # down
            (0, 1),
            (-1, 0),
            (0, -1)
        }

        memo = [[-1] * n_col for _ in range(n_row)] 

        def traverse(row: int, col: int) -> int:
            if memo[row][col] != -1:
                return memo[row][col]
            
            memo[row][col] = 1

            for row_change, col_change in directions:
                new_row = row_change + row
                new_col = col_change + col

                if (0 <= new_row < n_row and 
                    0 <= new_col < n_col and
                    matrix[row][col] < matrix[new_row][new_col]):
                    memo[row][col] = max(memo[row][col], 1 + traverse(new_row, new_col))
            
            return memo[row][col]
        
        answer = 1
        for i in range(n_row):
            for j in range(n_col):
                answer = max(answer, traverse(i, j))

        return answer



            