'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
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
        