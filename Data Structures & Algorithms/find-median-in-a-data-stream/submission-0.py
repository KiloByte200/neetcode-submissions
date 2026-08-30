import heapq
class MedianFinder:

    def __init__(self):
        self.top_half = [] # min heap
        self.bottom_half = [] # max heap

    def addNum(self, num: int) -> None:
        # 3 cases
        # if top and bottom half are both empty -> pick one and just populate it with num -> default to bottom
        # if one or the other is empty (if case above defaults to bottom we only worry about top -> empty, bottom -> populate) 
        # -> check if bottom root is less than num -> if so put in top_half else push to bottom
        # if both are populated -> we can basically do the same above

        # mechanism that decides where to push
        if not self.top_half and not self.bottom_half:
            heapq.heappush(self.bottom_half, -num)
            return
        
        if -self.bottom_half[0] >= num:
            heapq.heappush(self.bottom_half, -num)
        else:
            heapq.heappush(self.top_half, num)

        # mechanism that balances

        while len(self.top_half) - len(self.bottom_half) > 1: # means that top_half is bigger than bottom
            popped = heapq.heappop(self.top_half)
            heapq.heappush(self.bottom_half, -popped)

        while len(self.top_half) - len(self.bottom_half) < -1: # means that top_half is bigger than bottom
            popped = heapq.heappop(self.bottom_half)
            heapq.heappush(self.top_half, -popped)

        

    def findMedian(self) -> float:

        top_n = len(self.top_half)
        bot_n = len(self.bottom_half)

        if top_n == bot_n:
            return (self.top_half[0] - self.bottom_half[0]) / 2
        
        if top_n > bot_n:
            return self.top_half[0]

        return -self.bottom_half[0]
        
        