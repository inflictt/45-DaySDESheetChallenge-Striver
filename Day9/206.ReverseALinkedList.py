# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute idea is take the array get down all the values from in it to store into an array theen rev the arr and then make node to it againa nd done .

        # optimised ll idea is that 3 ptr curr , prev and upcoming/next so 
        # prev will start from none by default and the curr pting to head and 
        # next/upcom will point to head.next so 
        # then. the curr will point to prev , next -> curr and after evry itr we will mocve eery one ahead untill uppcom or next .next is null 
#  head = [1,2,3,4,5]
        prev = None 
        curr = head # points to 1 
         # points to 2
        while curr:
            upcoming = curr.next
            curr.next = prev #so both curr and prev are now none
            prev = curr #now pts to 1
            curr = upcoming  #now pts to 2
        head = prev
        return head
        
# pehele next ko save kraa
        # phir current.next ko pichle pr point kra
        # prev ko curr node assign kr diya
        # last mai curr. ko upcoming node dedi
        # in the end curr point to none and prev is the head
        
