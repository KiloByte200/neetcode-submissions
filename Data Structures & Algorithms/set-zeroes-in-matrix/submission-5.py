class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_col = set()
        zero_row = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_col.add(j)
                    zero_row.add(i)

        
        # set row to 0's
        for col in range(len(matrix[i])):
            for row in zero_row:
                matrix[row][col] = 0

    
        # set cols to 0
        for col in zero_col:
            for row in range(len(matrix)):
                matrix[row][col] = 0
        
                
                
        
        