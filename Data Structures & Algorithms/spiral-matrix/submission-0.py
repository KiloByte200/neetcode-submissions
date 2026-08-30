class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        newMatrix = []

        while left < right and top < bottom:

            for i in range(left, right):
                newMatrix.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom):
                newMatrix.append(matrix[j][right - 1])
            right -= 1
            
            if top < bottom:
                for k in range(right - 1, left - 1, -1):
                    newMatrix.append(matrix[bottom-1][k])
                bottom -= 1
            
            if left < right:
                for l in range(bottom - 1, top - 1, -1):
                    newMatrix.append(matrix[l][left])
                left += 1
        
        return newMatrix
