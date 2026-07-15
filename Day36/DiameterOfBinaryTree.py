# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0
            lf = solve(root.left)
            rt = solve(root.right)
            self.maxi = max(self.maxi,lf+rt)
            return 1+ max(lf,rt)
        self.maxi = 0
        solve(root)
        return self.maxi