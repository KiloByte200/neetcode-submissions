class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []
        intervals.sort(key=lambda interval: interval[0])
        mergedInterval = intervals[0]

        for interval in intervals[1:]:
          if mergedInterval[1] >= interval[0]:
              mergedInterval[1] = max(mergedInterval[1], interval[1])
          else:
              result.append(mergedInterval)
              mergedInterval = interval

        return result + [mergedInterval]
        