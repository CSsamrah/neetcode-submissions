# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=current=ListNode()
        # list1 and list2 are head of linkedlist

        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1    # save the address of list1 head
                list1=list1.next     # updates list1 head to the next element in list1
            else:
                current.next=list2
                list2=list2.next
            current=current.next  

        current.next=list1 or list2

        return dummy.next
        