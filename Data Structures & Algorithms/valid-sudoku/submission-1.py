class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMem = [set() for _ in range(9)]
        colMem = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

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
                    

                boxIndex = (r//3) * 3 + (c//3)
                if num in box[boxIndex]:
                    return False
                box[boxIndex].add(num)
                    
        return True


        