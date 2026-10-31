class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[1])
        result = 0

        previous_end = intervals[0][1]
        for interval in intervals[1:]:
            if previous_end <= interval[0]:
                previous_end = interval[1]
            else:
                result += 1
        
        return result
        