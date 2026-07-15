# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        level = 0
        ans = []
        while que:
            level +=1
            currLevelElms = []
            for i in range(len(que)):
                elem = que.popleft()
                currLevelElms.append(elem)
                if elem.left:
                    que.append(elem.left)
                if elem.right:
                    que.append(elem.right)
            # ans.append(currLevelElms)
            ans.append(currLevelElms[-1].val)
            # now i just have to add the last elem of currlevel elms arrahyt o ans array 
        return ans
