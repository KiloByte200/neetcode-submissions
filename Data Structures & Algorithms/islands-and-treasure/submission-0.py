from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        queue = deque()

        directions = [
            (1, 0), # down
            (0, 1), # right
            (-1, 0), # up
            (0, -1) # left

        ]

        # first pass for treasure
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            row, col, dist = queue.popleft()

            for row_change, col_change in directions:
                new_row = row_change + row
                new_col = col_change + col

                if (
                    0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[new_row]) and
                    grid[new_row][new_col] == 2147483647 
                ):
                    queue.append((new_row, new_col, dist+1))
                    grid[new_row][new_col] = dist+1
        




        