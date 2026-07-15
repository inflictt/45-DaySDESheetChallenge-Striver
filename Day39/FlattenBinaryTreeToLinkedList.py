# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def flat(root):
            if not root:
                return
            flat(root.left)
            flat(root.right)
            temp = root.right  # Save original right subtree
            root.right = root.left  # Move left subtree to right
            root.left = None

            curr = root
            while curr.right:
                curr = curr.right

            curr.right = temp  # Attach original right subtree

        if not root:
            return []
        if not root.left and not root.right:
            return root

        return flat(root)