# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def buildBST(
            preorder, bound
        ):  # i is the index itr over the arr preorder and bound is the root value/upper limit

            if self.i >= len(preorder):
                return
            val = preorder[self.i]
            if val > bound:
                return
            root = TreeNode(val)
            self.i += 1
            root.left = buildBST(preorder, root.val)
            root.right = buildBST(
                preorder, bound
            )  # for rigth bound would be the initialval passed
            return root

        self.i = 0
        bound = float("inf")
        return buildBST(preorder, bound)
