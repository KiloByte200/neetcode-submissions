import heapq
class MedianFinder:

    def __init__(self):
        self.top_half = [] # min heap
        self.bottom_half = [] # max heap

    def addNum(self, num: int) -> None:

        # Add to lower half
        heapq.heappush(self.bottom_half, -num)

        # add bottoms max to top
        popped = heapq.heappop(self.bottom_half)
        heapq.heappush(self.top_half, -popped)

        # mechanism that balances
        while len(self.top_half) > len(self.bottom_half): # means that top_half is bigger than bottom
            popped = heapq.heappop(self.top_half)
            heapq.heappush(self.bottom_half, -popped)

        

    def findMedian(self) -> float:

        if len(self.bottom_half) > len(self.top_half):
            return  -self.bottom_half[0]
        return (self.top_half[0] - self.bottom_half[0]) / 2
        
        