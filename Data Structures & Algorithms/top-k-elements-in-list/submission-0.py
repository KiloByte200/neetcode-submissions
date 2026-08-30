from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap key:number -> value: frequency
        # loop through nums and add freq to hashmap
        # loop through hashmap and append to list the answers

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        pq = []

        for key in freq:
            heapq.heappush(pq, (-freq[key], key))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])
        return result