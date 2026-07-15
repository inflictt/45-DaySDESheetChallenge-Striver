# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node,ans):
                if not node:
                    return
                left = inorder(node.left,ans)
                right = inorder(node.right,ans)
                ans.append(node.val)
                return ans
        if not root :
            return []
        ans = []
        new = inorder(root,ans)
        return ans