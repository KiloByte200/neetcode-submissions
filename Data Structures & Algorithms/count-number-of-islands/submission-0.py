class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = {
            (1, 0), # down
            (0, 1), # right
            (-1, 0), # up
            (0, -1), # left
        }

        def dfs(row: int, col: int) -> None:

            grid[row][col] = "#"

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    new_row < len(grid) and new_col < len(grid[new_row]) and
                    0 <= new_row and 0 <= new_col and
                    grid[new_row][new_col] == "1"
                ):
                    dfs(new_row, new_col)

        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "0" or grid[row][col] == "#":
                    continue
                
                islands += 1
                dfs(row, col)
        
        return islands
        