# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head

        # make slow start at the beginning, fast start n ahead of slow
        slow = node
        fast = node
        for _ in range(n):
            fast = fast.next
        
        # move until fast reaches the end of the LL
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the number
        if slow and slow.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return node.next
        