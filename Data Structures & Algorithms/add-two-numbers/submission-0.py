# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next



        # loop through each LL at the same time
        # add digits from both to node1 + carry
        # if greater than 10 -> % 10 and make a carry variable
        # if node2 is shorter than node1 -> unload while carry: on node1.next.val
        # if node 1 is shorter than node2 -> make node1.next = node2
        # if same length just stop


            


            

        

        