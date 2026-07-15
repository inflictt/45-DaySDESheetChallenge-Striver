'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        que = deque([(root, 0)])   # (node, horizontal distance)
        ansDict = {}
        while que:
            currVal, currLevel = que.popleft()
            # overwrite every time
            if currLevel not in ansDict:
                ansDict[currLevel] = currVal.data
            if currVal.left:
                que.append((currVal.left, currLevel - 1))
            if currVal.right:
                que.append((currVal.right, currLevel + 1))
        ans = []
        for hd in sorted(ansDict):
            ans.append(ansDict[hd])

        return ans