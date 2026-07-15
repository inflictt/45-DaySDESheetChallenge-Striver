# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute stroe all the elm in an areey and ®eturn
        que = deque([root])
        ans = []
        while que:
            currLvl = []
            for i in range(len(que)):
                elem = que.popleft()
                currLvl.append(elem.val)
                if elem.left:
                    que.append(elem.left)
                if elem.right:
                    que.append(elem.right)
            ans.extend(currLvl)
        ans = sorted(ans)
        return ans[k - 1]
