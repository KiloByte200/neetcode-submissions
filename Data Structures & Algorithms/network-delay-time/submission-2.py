from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)

        for edge1, edge2, time in times:
            adj_list[edge1].append((edge2, time))
        

        time_counter = {}


        def dfs(node: int, time:int) -> None:
            nonlocal time_counter
            
            if node not in time_counter:
                time_counter[node] = time
            elif time_counter[node] <= time:
                return
            else:
                time_counter[node] = min(time_counter[node], time)


            for new_node, new_time in adj_list[node]:
                dfs(new_node, new_time + time_counter[node])
        
        dfs(k, 0)

        if len(time_counter.keys()) != n:
            return -1
        
        max_time = 0
        for val in time_counter.values():
            max_time = max(max_time, val)
        return max_time
