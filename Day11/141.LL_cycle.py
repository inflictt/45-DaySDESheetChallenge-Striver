# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tried solving the detect the node where cycle starts - to check a loop in ll we have to use tort and hare app and after they both f and s meet stop both and take one temp var start iterating that from head and the stopped slow ptr by 1 1 steps and wehre they both meet is the cycle detection pt 
        slow , fast = head,head
        while fast and fast.next:#keep itr untill this condititon comes false
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True #means cycle detected
        return False 