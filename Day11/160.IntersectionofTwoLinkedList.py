# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            # so now i have the lens
            # if len of a is more then get the db and loop that much to get their else b's len is more so do for that
            nA = 0
            tempA = headA
            while tempA:
                nA += 1
                tempA = tempA.next

            nB = 0
            tempB = headB
            while tempB:
                nB += 1
                tempB = tempB.next
            tempA = headA
            tempB = headB
            # so the above has got the len to me 
            if nA > nB:
                for _ in range(nA - nB):
                    tempA = tempA.next
            else:
                for _ in range(nB - nA):
                    tempB = tempB.next
            # thiis above made the length / starting same 
            # and this below got the equality node checks
            while tempA != tempB:
                tempA = tempA.next
                tempB = tempB.next

            return tempA