# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        tail=temp = head
        n = 0
        while tail:
            n+=1
            tail = tail.next
        k = k%n #optimisation as k==n will have the same 
        if  k ==0 :
            return head
       
        # tail.next = head
        
        
        goUptoForNewHead = n-k#5-2 =3

        for i in range(goUptoForNewHead-1):
            temp =temp.next
        # now this temp will go upto node 3(1->2->3)
        newHead = temp.next
        temp.next = None
        new = newHead
        while new.next:
            new = new.next
        new.next = head
        return newHead
