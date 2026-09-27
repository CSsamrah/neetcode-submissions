# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head

        left=dummy
        right=dummy

        for _ in range(n+1):
            right=right.next
        
        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next



        # count=0
        # temp=head
        # while temp:
        #     count+=1
        #     temp=temp.next
        # if count==n:
        #     return head.next
        # temp=head
        # for _ in range(count-n-1):
        #     temp=temp.next
        # temp.next=temp.next.next
        # return head



