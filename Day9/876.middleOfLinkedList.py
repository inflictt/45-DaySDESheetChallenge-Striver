# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #    Brute Force: Traverse the linked list, count the number of nodes, then traverse again to the middle node. Time: O(n), Space: O(n) if storing nodes in an array).

    #     Optimal (Tortoise and Hare): Use two pointers:
    #     slow moves 1 step at a time.
    #     fast moves 2 steps at a time.
    #     When fast reaches the end (or cannot move further), slow will be at the middle node.
        fast , slow = head,head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        return slow