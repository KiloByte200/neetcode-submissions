# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = list1 if list1 else list2
        if list1 and list2:
            head = list1 if list1.val <= list2.val else list2


        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                while pointer1.next and pointer1.next.val <= pointer2.val:
                    pointer1 = pointer1.next
                temp = pointer1.next
                pointer1.next = pointer2

                pointer1 = temp
            else:
                while pointer2.next and pointer2.next.val <= pointer1.val:
                    pointer2 = pointer2.next
                temp = pointer2.next
                pointer2.next = pointer1

                pointer2 = temp
        
        return head

        