# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        ans = []#my final arr in which each lvl of elm will be added later
        lvl =  0
        while que:
            lvl +=1
            currLvl = [ ]
            for i in range(len(que)):
                curr = que.popleft()
                currLvl.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            ans.append(currLvl)
        return ans