class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        seen = set()
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1),   # right
        ]

        def backtracking(row: int, col: int, index: int):
            if index >= len(word):
                return True

            seen.add((row, col))

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[new_row]):
                    if (new_row, new_col) not in seen:
                        if board[new_row][new_col] == word[index]:
                            if backtracking(new_row, new_col, index+1):
                                return True
            seen.remove((row, col))
            return False
                    
                
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 1):
                        return True
        
        return False
        