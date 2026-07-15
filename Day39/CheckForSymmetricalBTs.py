# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def bfs(root):
            if not root:
                return []

            que = deque([root])
            ans = []

            while que:
                currLvl = []

                for _ in range(len(que)):
                    elem = que.popleft()

                    if elem is None:
                        currLvl.append(None)
                        continue

                    currLvl.append(elem.val)
                    que.append(elem.left)
                    que.append(elem.right)

                ans.append(currLvl)

                # Stop when next level has only None nodes
                if all(x is None for x in que):
                    break

            return ans

        leftArr = bfs(root.left)
        rightArr = bfs(root.right)

        if len(leftArr) != len(rightArr):
            return False

        for i in range(len(leftArr)):
            if leftArr[i] != rightArr[i][::-1]:
                return False

        return True
