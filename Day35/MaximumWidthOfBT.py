# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so ill do bfs and for all none values ill add dollar sign
        if not root:
            return []
        que = deque([(root, 0)])
        level = 0 
        ans = 1
        # (2*index)+1 #formula for left indexing
        # (2*index)+2 #formula for right indexing
        while que:
            currLevelNodes = []
            for _ in range(len(que)):
                elm, idx = que.popleft()
                currLevelNodes.append((elm, idx))
                if elm.left:
                    que.append((elm.left, (2 * idx) + 1))
                if elm.right:
                    que.append((elm.right, (2 * idx) + 2))
            width = currLevelNodes[-1][1] - currLevelNodes[0][1] + 1
            ans = max(ans, width)
        return ans