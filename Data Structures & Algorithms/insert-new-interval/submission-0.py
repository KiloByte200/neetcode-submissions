class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newIntervals = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:  # interval to the left of NewInterval
                newIntervals.append(interval)
            elif interval[0] > newInterval[1]: # interval is to the right of NewInterval
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            else:  # overlap detected
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        return newIntervals + [newInterval]
        