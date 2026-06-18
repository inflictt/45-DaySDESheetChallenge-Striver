# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # so we have one carry ptr and one check fo tkaing modulo % finiding the rem so ew that would be the val in the node
        # l1 -> 9->9->9 and l2 -> 9->9
        carry = 0 
        dummy= tail = ListNode()
        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            ttl = x + y + carry
            carry = ttl // 10
            digit = ttl % 10

            tail.next= ListNode(digit) #8 with carry as 1
            tail = tail.next
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        return dummy.next