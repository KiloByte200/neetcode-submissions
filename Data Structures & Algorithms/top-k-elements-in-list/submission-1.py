from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap key:number -> value: frequency
        # loop through nums and add freq to hashmap
        # loop through hashmap and append to list the answers

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)


        result = []
        for count in range(len(buckets)-1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result