''' Structure for tree and linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''
class Solution:
    def treeToDLL(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inArr.append(root)
            inorder(root.right)
        # code here
        # so prev node would be my None node for the first tree examolea dn the
        # node ==2 value would be inorder first node so curr adn next woul bde be
        # next would be teh node ==1 value adn then cfter that crur becoms 1 adn enxt would becom three same 
        self.inArr = []
        inorder(root)
        # so till here my inorder arr has been formed
        # now i ihave ort start iterating 
        head = self.inArr[0]
        prev = None
        nxt = head
        
        
        for i in range(0,len( self.inArr)):
            currNode = self.inArr[i]    #node initilaisaiton         
            currNode.left = prev    #this goes back 
            prev = currNode #prev node updated evrytime 
            # inbound cehck foir the next elem
            if i < len(self.inArr)-1:
                nxt = self.inArr[i+1]
            else:
                nxt = None
             #this goes for the next node
            currNode.right = nxt
        # last node make sure to be poitning ot none
        currNode.right = None
        return head
            