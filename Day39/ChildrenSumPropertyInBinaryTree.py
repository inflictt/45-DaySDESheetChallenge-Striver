'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        if not root:
            return True
        que = deque([root])
        lvl = 0
        while que:
            lvl +=1
            for i in range(len(que)):#only 1 in start
                targetNode = que.popleft() #35 pop hogyi
                targetNodeKaLeft = 0
                targetNodeKaRight = 0
                if not targetNode.left and not targetNode.right:
                    continue
                if targetNode.left:
                    targetNodeKaLeft = targetNode.left.data
                    que.append(targetNode.left)
                if targetNode.right:
                    targetNodeKaRight = targetNode.right.data
                    que.append(targetNode.right)
                if targetNodeKaLeft+targetNodeKaRight == targetNode.data:#means 20+15 is 35 or ont yes
                    continue
                else:#not reutnr False
                    return False
        return True   
                    
                    
                    
                    
                    