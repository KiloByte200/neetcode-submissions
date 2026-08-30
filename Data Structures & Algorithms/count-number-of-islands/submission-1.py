class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = {
            (1, 0), # down
            (0, 1), # right
            (-1, 0), # up
            (0, -1), # left
        }
        
        

        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "0" or grid[row][col] == "#":
                    continue
                
                islands += 1

                stack = [(row, col)]
                grid[row][col] = "#"

                while stack:
                    curr_row, curr_col = stack.pop()

                    for row_change, col_change in directions:
                        new_row = curr_row + row_change
                        new_col = curr_col + col_change

                        if (
                            new_row < len(grid) and new_col < len(grid[new_row]) and
                            0 <= new_row and 0 <= new_col and
                            grid[new_row][new_col] == "1"
                        ):
                            stack.append((new_row, new_col))
                            grid[new_row][new_col] = "#"
        
        return islands
        