# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def search(node, target, curr):
            if not node:
                return False

            # Found the target and it's not the same node
            if node.val == target:
                return node != curr

            if target < node.val:
                return search(node.left, target, curr)
            else:
                return search(node.right, target, curr)

        def dfs(node):
            if not node:
                return False
            target = k - node.val
            if search(root, target, node):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right

        return dfs(root)
