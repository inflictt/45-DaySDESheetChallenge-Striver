# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # odd even odd even fomratting like first odd is l to r and then r to l
        if not root:
            return []
        que = deque([root])
        lvl = 0
        ans = []
        while que:
            lvl +=1 #odd is l to r nothing to change
            currLevel = []
            for i in range(len(que)):
                elem =  que.popleft()
                currLevel.append(elem.val)
                if elem.left:
                    que.append(elem.left)
                if elem.right:
                    que.append(elem.right)
            if lvl %2==0:#store in reverse
                currLevel.reverse()
            ans.append(currLevel)
        return ans