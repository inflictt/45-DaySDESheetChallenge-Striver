# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order must be sorted/ ig
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.ans.append(root.val)
            inorder(root.right)

        self.ans = []
        inorder(root)
        for i in range(len(self.ans) - 1):
            if self.ans[i] >= self.ans[i + 1]:
                return False

        return True
