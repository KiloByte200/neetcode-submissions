import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapq.heapify(self.heap)
        n = len(self.heap)

        for _ in range(n-k):
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) != 0 and self.heap[0] >= val:
            return self.heap[0]
        while len(self.heap) >= self.k:
            heapq.heappop(self.heap)

        heapq.heappush(self.heap, val)
        return self.heap[0]
