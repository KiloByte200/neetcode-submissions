from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.__stamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__stamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.__stamps[key]

        start = 0
        end = len(timestamps) - 1
        res = ""

        while start <= end:
            mid = (end - start) // 2 + start

            if timestamps[mid][0] <= timestamp:
                res = timestamps[mid][1]
                print(res)
                start = mid + 1
            else:
                end = mid - 1
                
        return res
            
