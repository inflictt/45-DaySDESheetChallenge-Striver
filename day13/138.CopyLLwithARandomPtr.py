# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        # we will add a corresponding node to curr node so each node
        # will have their copy node in their next pointer
        curr = head
        while curr:
            currNext = curr.next      # real A -> B
            curr.next = Node(curr.val) # A -> X
            curr.next.next = currNext # A -> X -> B

            curr = currNext
        curr = head

        while curr and curr.next:
            if curr.random == None:
                # real waala hi none hai toh x->random bhi none
                curr.next.random = None
            else:
                # if A.random points to C then X.random should point to C's copy
                curr.next.random = curr.random.next
            curr = curr.next.next
        # now separation of LL
        newHead = head.next
        curr = head          # original list pointer
        newCurr = newHead    # copied list pointer
        while curr and newCurr:
            # directly A -> B point kro skipping X
            curr.next = curr.next.next
            # directly X -> Y point kro skipping B
            if newCurr.next:
                newCurr.next = newCurr.next.next
            else:
                newCurr.next = None
            curr = curr.next
            newCurr = newCurr.next
        return newHead