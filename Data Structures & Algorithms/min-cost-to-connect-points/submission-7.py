class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_points = [float("inf")] * n
        min_points[0] = 0

        in_web = [False] * n
        i = 0

        while i < n:
            in_web[i] = True
            xi, yi = points[i]

            smallest_edge = n

            for j in range(1, n):
                if in_web[j]:
                    continue
                xj, yj = points[j]

                cand = abs(xi-xj) + abs(yi-yj)
                min_points[j] = min(min_points[j], cand)
                
                if smallest_edge >= n or min_points[j] < min_points[smallest_edge]:
                    smallest_edge = j
            
            i = smallest_edge
        
        return sum(min_points)

        