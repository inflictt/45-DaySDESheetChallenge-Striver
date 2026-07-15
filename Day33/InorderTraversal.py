# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            # If there is no left child
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            else:
                # Find the rightmost node in left subtree
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                # Create temporary thread
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                # Remove thread and visit node
                else:
                    prev.right = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans