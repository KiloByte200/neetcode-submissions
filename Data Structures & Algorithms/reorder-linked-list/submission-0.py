# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        # reverse second half
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        # prev is head of reversed second half
        # head is head of normal first half

        # now interweave lists
        while prev:
            temp = head.next
            head.next = prev

            temp2 = prev.next
            prev.next = temp

            head = temp
            prev = temp2
        
        