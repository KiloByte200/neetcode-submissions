class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])

        start_row = 0
        end_row = h - 1

        while start_row <= end_row:
            mid_row = (end_row - start_row) // 2 + start_row
            
            if matrix[mid_row][0] <= target <= matrix[mid_row][w - 1]:
                start_col = 0
                end_col = w -1

                while start_col <= end_col:
                    mid_col = (end_col - start_col) // 2 + start_col

                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        start_col = mid_col + 1
                    else:
                        end_col = mid_col - 1
                        
                return False
            elif matrix[mid_row][0] > target:
                end_row = mid_row - 1
            else:
                start_row = mid_row + 1
            
        return False

        