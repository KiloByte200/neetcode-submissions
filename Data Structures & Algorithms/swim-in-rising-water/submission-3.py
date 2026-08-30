import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # Bi directional DFS? choose the smallest adjacent edge every time?
        # but not just the smallest adjacent to the farthest square but smallest adjacent across any square
        # Perhaps it is BFS where we push an order of smallest grid space adjacent to the current to largest to the queue


        # begin_frontier set will store row and col of starting points, then will accumulate adjacent edges
        
        directions = [
            (1, 0), # down
            (0, 1), # right
            (-1, 0), # up
            (0, -1) # left
        ]

        frontier_heap = []
        heapq.heapify(frontier_heap)

        heapq.heappush(frontier_heap, (grid[0][0], (0, 0)))
        visited = {(0, 0)}

        while frontier_heap:
            max_elevation, (row, col) = heapq.heappop(frontier_heap)

            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return max_elevation

            for row_change, col_change in directions:
                new_row = row_change + row
                new_col = col_change + col

                if (
                    0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[new_row]) and
                    (new_row, new_col) not in visited
                ):
                    new_max_elevation = max(max_elevation, grid[new_row][new_col])
                    heapq.heappush(frontier_heap, (new_max_elevation, (new_row, new_col)))
                    
                    visited.add((new_row, new_col))
        
        return 0

