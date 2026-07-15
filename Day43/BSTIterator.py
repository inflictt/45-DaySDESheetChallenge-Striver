# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.ans = []
        self.inorder(root)
        self.index = -1

    def next(self) -> int:  # this function give the current lowest in the full tree
        self.index += 1
        return self.ans[self.index]

    def hasNext(self) -> bool:  # cehck if we can move to next or not
        if self.index + 1 < len(self.ans):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
