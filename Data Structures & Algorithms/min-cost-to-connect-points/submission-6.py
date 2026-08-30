class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        min_points = [float("inf")] * len(points)
        min_points[0] = 0

        in_web = {0}
        i = 0

        while i < len(points):
            xi, yi = points[i]

            smallest_edge = len(points)

            for j in range(1, len(points)):
                if j in in_web:
                    continue
                xj, yj = points[j]

                cand = abs(xi-xj) + abs(yi-yj)
                min_points[j] = min(min_points[j], cand)
                
                if smallest_edge >= len(points) or min_points[j] < min_points[smallest_edge]:
                    smallest_edge = j
            
            in_web.add(smallest_edge)
            i = smallest_edge
        
        return sum(min_points)

        