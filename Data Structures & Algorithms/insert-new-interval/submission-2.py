class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:  # interval to the left of NewInterval
                result.append(interval)

            elif interval[0] > newInterval[1]: # interval is to the right of NewInterval
                return result + [newInterval] + intervals[i:]
            
            else:  # overlap detected
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        return result + [newInterval]
        