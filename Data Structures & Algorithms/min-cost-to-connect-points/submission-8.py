class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_points = [float("inf")] * n
        min_points[0] = 0

        in_web = [False] * n
        i = 0
        result = 0

        for _ in range(n):
            in_web[i] = True
            result += min_points[i]

            xi, yi = points[i]

            smallest_edge = -1

            for j in range(n):
                if in_web[j]:
                    continue
                xj, yj = points[j]

                cand = abs(xi-xj) + abs(yi-yj)
                min_points[j] = min(min_points[j], cand)
                
                if smallest_edge == -1 or min_points[j] < min_points[smallest_edge]:
                    smallest_edge = j
            
            i = smallest_edge
        
        return result

        