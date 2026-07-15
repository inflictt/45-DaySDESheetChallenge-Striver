'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        # first going left only 
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.data]
        def leftBoundary(node):
            if not node:
                return
            # Stop at leaves
            if not node.left and not node.right:
                return
            left.append(node.data)
            if node.left:
                leftBoundary(node.left)
            else:
                leftBoundary(node.right)
        
        def middleBoundary(node):
            if not node:
                return
        
            if not node.left and not node.right:
                middle.append(node.data)
                return
            if node.left:
                middleBoundary(node.left)
            if node.right:
                middleBoundary(node.right)
        
        def rightBoundary(node):
            if not node:
                return
            # Stop at leaves
            if not node.right and not node.left:
                return
            right.append(node.data)
            if node.right:
                rightBoundary(node.right)
            else:
                rightBoundary(node.left)
        
        
        left , middle , right = [],[],[]
        ans = [root.data]
        leftBoundary(root.left)
        middleBoundary(root)
        rightBoundary(root.right)
        ans.extend(left)
        ans.extend(middle)
        right.reverse()
        ans.extend(right)
        return ans