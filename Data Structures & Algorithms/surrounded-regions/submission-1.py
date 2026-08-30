from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[rows-1])

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        queue = deque()

        # left and right edges
        for row in range(rows):
            if board[row][0] == "O":
                queue.append((row, 0))
                board[row][0] = "#"
            
            if board[row][cols-1] == "O":
                queue.append((row, cols-1))
                board[row][cols-1] = "#"

        # top and bottom edges
        for col in range(1, cols-1):
            if board[0][col] == "O":
                queue.append((0, col))
                board[0][col] = "#"
            
            if board[rows-1][col] == "O":
                queue.append((rows-1, col))
                board[rows-1][col] = "#"


        # BFS
        while queue:
            row, col = queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    board[new_row][new_col] == "O"
                ):
                    queue.append((new_row, new_col))
                    board[new_row][new_col] = "#"
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"

