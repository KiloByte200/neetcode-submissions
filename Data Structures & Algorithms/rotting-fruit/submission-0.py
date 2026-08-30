from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        count = 0
        queue = deque()

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    count +=1
                elif grid[row][col] == 2:
                    queue.append((row, col))

        time = 0
        while queue and count > 0:
            fruits_this_minute = len(queue)

            for _ in range(fruits_this_minute):
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if (
                        0 <= new_row < len(grid) and
                        0 <= new_col < len(grid[new_row]) and
                        grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        count -= 1
                        queue.append((new_row, new_col))
            time += 1




        if count > 0:
            return -1
        return time
            