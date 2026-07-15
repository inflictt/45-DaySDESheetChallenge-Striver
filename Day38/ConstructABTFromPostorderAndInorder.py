# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        # Last element of postorder is always the root
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        
        rootIndex = inorder.index(rootVal)

        # Left part of inorder 
        leftInorder = inorder[:rootIndex]
        # Number of nodes in the left subtree = rootIndex
        leftPostorder = postorder[:rootIndex]
        # Right part of inorder
        rightInorder = inorder[rootIndex + 1:]
        rightPostorder = postorder[rootIndex:-1]
        # Build left subtree
        root.left = self.buildTree(leftInorder, leftPostorder)
        # Build right subtree
        root.right = self.buildTree(rightInorder, rightPostorder)

        return root