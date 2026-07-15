class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  # empty tree
            return root
        while root:
            if root.val == val:  # found — return the subtree
                return root
            elif root.val > val:  # target smaller → go left
                root = root.left
            else:  # target larger → go right
                root = root.right
        return None  # val not in tree
