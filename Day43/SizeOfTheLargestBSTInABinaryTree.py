''' Structure of a Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Info:
    def __init__(self, minVal, maxVal, size):
        self.minVal = minVal
        self.maxVal = maxVal
        self.size = size


class Solution:

    def largestBst(self, root):
        return self.helper(root).size

    def helper(self, root):

        # Empty tree is a BST of size 0
        if not root:
            return Info(float('inf'), float('-inf'), 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        # Current subtree is a BST
        if root.data > left.maxVal and root.data < right.minVal:

            currMin = min(root.data, left.minVal)
            currMax = max(root.data, right.maxVal)
            currSize = left.size + right.size + 1

            return Info(currMin, currMax, currSize)

        # Current subtree is NOT a BST
        return Info(
            float('-inf'),
            float('inf'),
            max(left.size, right.size)
        )