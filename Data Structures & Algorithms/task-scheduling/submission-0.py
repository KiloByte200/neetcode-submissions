from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0
        task_queue = deque([])

        task_counter = Counter(tasks)
        heap = [-freq for freq in task_counter.values()]
        heapq.heapify(heap)

        while task_queue or heap:
            cycle += 1
            
            if task_queue:
                if cycle == task_queue[0][0]:
                    _, new_freq = task_queue.popleft()
                    heapq.heappush(heap, -new_freq)
            
            if heap:
                popped_process_freq = -heapq.heappop(heap) - 1
                if popped_process_freq > 0:
                    task_queue.append((cycle+n+1, popped_process_freq))
        
            
        
        return cycle