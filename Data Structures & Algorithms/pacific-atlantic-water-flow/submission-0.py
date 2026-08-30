from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        result = []

        atlantic_queue = deque()
        pacific_queue = deque()
        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        for row in range(rows-1):
            atlantic_queue.append((row, cols-1))
        for col in range(cols):
            atlantic_queue.append((rows-1, col))

        for row in range(rows):
            pacific_queue.append((row, 0))
        for col in range(1, cols):
            pacific_queue.append((0, col))

        pacific_seen = set(pacific_queue)
        atlantic_seen = set(atlantic_queue)

        while atlantic_queue:
            row, col = atlantic_queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    not (new_row, new_col) in atlantic_seen and
                    heights[row][col] <= heights[new_row][new_col]
                ):
                    atlantic_seen.add((new_row, new_col))
                    atlantic_queue.append((new_row, new_col))

        while pacific_queue:
            row, col = pacific_queue.popleft()

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    not (new_row, new_col) in pacific_seen and
                    heights[row][col] <= heights[new_row][new_col]
                ):
                    pacific_seen.add((new_row, new_col))
                    pacific_queue.append((new_row, new_col))


        return [[row, col] for row, col in pacific_seen & atlantic_seen]








        