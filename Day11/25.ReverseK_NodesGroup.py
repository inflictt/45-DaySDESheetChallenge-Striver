# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevHead , currHead = None , head
        curr , prev= head ,None
        n = 0
        temp = head
        while temp : 
            n+=1
            temp=temp.next
        ans = None
        groups = n//k #if 1,2,3,4,5,6,7,8,9 groups = 3
        for _ in range(0,groups):
            prev = None # to be declared for every grp
            for i in range(0,k):#just for the frist k elem lets settle the group 1 frirst
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr  =nextNode
            #  now in this my idea is that when the array part 1 will be reversed 
            # 3   ->   2->    1 ->>  |   4->>>
# PH(null)   prev             ch(at 1).  curr
#in case # PH(null)  so now as ph-> to null ill make it pnt to cH and the ch to cur
# else ph.next->prev and  ch to cur
            if prevHead == None:
                ans = prev
            else:#prevhead is not none and pts to a node
                prevHead.next = prev
            currHead.next = curr
            prevHead = currHead
            currHead = curr
        return ans