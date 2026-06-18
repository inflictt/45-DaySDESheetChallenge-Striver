# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # bette approach is that i move the ptr temp utpo n times in the ll 
        # and then ill reach the node whose .next -> .next.next from itself
        fast = head 
        slow = head 
        if n==1 and head.next==None:
            return head.next
        
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            fast=fast.next
            slow = slow.next

        slow.next=  slow.next.next

        return head