class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMem = [set() for _ in range(9)]
        colMem = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue

                num = board[r][c]
                if num in rowMem[r]:
                    return False
                rowMem[r].add(num)
                    
                
                if num in colMem[c]:
                    return False
                colMem[c].add(num)
                    

                boxRow = r // 3
                boxCol = c //3
                if num in box[boxRow][boxCol]:
                    return False
                box[boxRow][boxCol].add(num)
                    
        return True


        