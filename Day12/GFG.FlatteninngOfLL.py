'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):

        def getMid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second = slow.next
            slow.next = None

            return second
            
        # this above func gve me the starting of my second parrted nodes 
        # this merge combine combines and give me the fnal sorted ll
        
        def mergeCombine(left, right):
            dummy = Node(0)
            tail = dummy

            while left and right:
                if left.data < right.data:
                    tail.bottom = left
                    left = left.bottom
                else:
                    tail.bottom = right
                    right = right.bottom
                tail = tail.bottom
                tail.next = None
            if left:
                tail.bottom = left
            if right:
                tail.bottom = right
            return dummy.bottom

        def mergeLL(head):
            if not head or not head.next:
                return head
            right = getMid(head)
            left = head
            left = mergeLL(left)
            right = mergeLL(right)
            return mergeCombine(left, right)

        return mergeLL(root)