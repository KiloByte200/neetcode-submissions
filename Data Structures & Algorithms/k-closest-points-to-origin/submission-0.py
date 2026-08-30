import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-(x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result
        