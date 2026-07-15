'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        # dfs i wantw
        def solve(root,x):
            if not root:
                return
            if x<root.data:#as we need ceil adn root values i biggers #exlpplor left
            # so root val is one of our anwswwer
                self.ans = min(self.ans,root.data)#as value chahiye butt just bigger thn x not the biggerst value of the tree
                if root.left:
                    solve(root.left, x)
                return 
                
            elif x==root.data:#exart value mil gyi
                self.ans =  root.data
                return 
            else: #x bigger than ndoe value so exlplore eirght
                if root.right:
                    solve(root.right, x)
                return 
        
            
        self.ans = float('inf')
        solve(root,x)
        if self.ans!=float('inf'):
            return self.ans
        else:
            return -1