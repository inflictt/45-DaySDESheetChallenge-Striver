# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # opitmal -> laready sorted just 2 pts like ll1 and ll2 adn i and j and comparing and adding nodes proerply in asceding manner then if one list is short having if. else stat would worksd and directly point to array having nodes left 
        l1, l2 = list1,list2
        tail = dummy = ListNode()
        while l1 and l2:#mean go upto until one reached to none/tail/last
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next