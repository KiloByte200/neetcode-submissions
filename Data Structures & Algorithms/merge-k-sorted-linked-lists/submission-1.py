# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0

        # populate initial heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        dummy = ListNode()
        curr = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

            curr.next = node
            curr = curr.next
            curr.next = None
        
        return dummy.next


        