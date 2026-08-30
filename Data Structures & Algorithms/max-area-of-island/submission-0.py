class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        directions = [
            (1, 0), # right
            (0, 1), # down
            (-1, 0), # left
            (0, -1) # up
        ]

        maxIslandArea = 0


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 1:
                    continue
                
                stack = [(row, col)]
                grid[row][col] = 0

                candidate = 1

                while stack:
                    curr_row, curr_col = stack.pop()

                    for row_change, col_change in directions:
                        new_row = curr_row + row_change
                        new_col = curr_col + col_change

                        if (
                            0 <= new_row < len(grid) and
                            0 <= new_col < len(grid[row]) and
                            grid[new_row][new_col] == 1
                        ):
                            candidate += 1
                            stack.append((new_row, new_col))
                            grid[new_row][new_col] = 0


                maxIslandArea = max(maxIslandArea, candidate)
        
        return maxIslandArea