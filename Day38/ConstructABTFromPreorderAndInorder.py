# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(preorder, inorder, start, end):
            if start > end:
                return None

            rootVal = preorder[self.idx]  # first most elm of preorder #3
            rootValIdx = inorder.index(rootVal)  # got hte index in inorder arr =>1
            self.idx += 1  # as for recursion we dont check for 0 again so +1
            root = TreeNode(rootVal)
            root.left = solve(preorder, inorder, start, rootValIdx - 1)
            root.right = solve(preorder, inorder, rootValIdx + 1, end)
            return root

        self.idx = 0
        return solve(preorder, inorder, 0, len(inorder) - 1)
