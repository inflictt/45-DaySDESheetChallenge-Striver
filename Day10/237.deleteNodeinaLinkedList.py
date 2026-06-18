# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # copynext val in to currnode given
        new = node.next
        nextVal = new.val
        node.val = nextVal
        node.next = node.next.next