import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            first_stone = heapq.heappop(heap)
            second_stone = heapq.heappop(heap)

            new_stone = first_stone - second_stone
            if new_stone != 0:
                heapq.heappush(heap, new_stone)
         
        return -heap[0] if heap else 0
        