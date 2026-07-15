# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,target,arr):
            if not root :
                return 
            arr.append(root.val)
            if root == target:
                return True
            if dfs(root.left,target,arr):
                return True
            if dfs(root.right,target,arr):
                return True
            arr.pop()#removing parts not req
            return False
        # arr = []
        pArr = []
        qArr = []

        dfs(root, p, pArr)
        dfs(root, q, qArr)
        # final check
        ans = None
        for i in range(min(len(pArr), len(qArr))):
            if pArr[i] == qArr[i]:
                ans = pArr[i]
            else:
                break
        newNode = TreeNode(ans)
        return newNode