'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, x):
        #code here
        def floor(root,x):
            # if not root:
            #     return
            if root.data<x:#means propble floor for x
                self.ans = max(root.data,self.ans) #floor req but nearest to x so max
                # now go rigth as lefgt to 10 would be all less than 10
                if root.right:
                    floor(root.right,x)
            elif root.data==x:#equal than return itself only
                self.ans = root.data
                return 
            else:#root ki val jyada hai toh left jaao ab
                if root.left:
                    floor(root.left,x)
        self.ans = -float('inf')
        floor(root,x)
        if  self.ans != -float('inf'):
            return self.ans
        return -1