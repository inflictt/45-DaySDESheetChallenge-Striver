# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tried solving the detect the node where cycle starts - to check a loop in ll we have to use tort and hare app and after they both f and s meet stop both and take one temp var start iterating that from head and the stopped slow ptr by 1 1 steps and wehre they both meet is the cycle detection pt 

        temp = slow=fast=head
        
        if head==None or temp.next==None :
            return None
        # to check the cycle exists or not
        while fast and fast.next:
            fast = fast.next.next
            slow=slow.next
            if fast==slow:
                break
        if fast!=slow:#means no cycle detected early exit
            return None
        # finding where the cycle starts
        while temp:
            if temp==slow:
                break
            temp = temp.next
            slow = slow.next
        return temp