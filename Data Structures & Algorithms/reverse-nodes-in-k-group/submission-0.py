# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # slow and fast pointers start at head
        # fast pointer moves forward k amount
        #   if fast pointer is not able to move forward k amount end reversal loop
        # reverse linked list up until reaching the fast pointer
        #   this can be done using the textbook prev, curr loop
        
        dummy = ListNode(0, head)
        before_slow = dummy
        slow, fast = head, head


        while fast:

            forward = k
            while forward > 0 and fast:
                fast = fast.next
                forward -= 1

            if forward > 0:
                break
            
            prev = fast
            curr = slow
            while curr and curr != fast:
                nxt = curr.next
                curr.next = prev

                prev = curr
                curr = nxt
            
            before_slow.next = prev

            before_slow = slow
            slow = fast

        return dummy.next