# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        slow = head
        fast = head
        prev = None
        # get the len

        while fast and fast.next:
            fast = fast.next.next
            newNext = slow.next #next node for slow 
            slow.next = prev
            prev = slow
            slow =newNext

        # so after opti 
        # if fast==None:#got the list having even amt of node so do nothing
        if fast !=None:#odd length got 
            slow = slow.next
        while prev :#not none tk itr it
            if prev.val == slow.val :#move
                prev = prev.next
                slow = slow.next
            else:
                return False
        
        return True

        # how can i optim. this: 
        # fast == None → even length
        # fast != None → odd length