"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return
        que = deque([root])
        while que:
            prev = None

            for i in range(len(que)):
                curr = que.popleft()  # 3 we can say
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                if prev:  # means it not none
                    prev.next = curr
                prev = curr  # updated the prv
        return root
