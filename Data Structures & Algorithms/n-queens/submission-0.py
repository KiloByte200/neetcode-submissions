class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []
        curr = [["."] * n for _ in range(n)]

        columns = set()
        down_right_diag = set() # row - col
        down_left_diag = set() # row + col

        def backtrack(row: int):
            if row == n:
                result.append([''.join(board_row) for board_row in curr])
                return
            
            for i in range(len(curr[row])):
                if (
                    i in columns or
                    (row - i) in down_right_diag or 
                    (row + i) in down_left_diag
                ):
                    continue

                curr[row][i] = 'Q'
                columns.add(i)
                down_right_diag.add(row - i)
                down_left_diag.add(row + i)

                backtrack(row + 1)

                curr[row][i] = '.'
                columns.remove(i)
                down_right_diag.remove(row - i)
                down_left_diag.remove(row + i)
        
        backtrack(0)
        return result
            



        