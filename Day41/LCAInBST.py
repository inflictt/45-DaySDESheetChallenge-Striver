# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def solve(root, target, path):
            if not root:
                return False

            path.append(root)

            if root == target:
                return True

            if solve(root.left, target, path):
                return True
            if solve(root.right, target, path):
                return True

            # pop isliye ki us side mai na toh left waali value kaam na right ki
            path.pop()
            return False

        pArr, qArr = [], []
        solve(root, p, pArr)
        solve(root, q, qArr)

        pL, qL = len(pArr), len(qArr)
        if pL == 0:
            return None
        if qL == 0:
            return None
        ans = None
        for i in range(min(pL, qL)):
            if pArr[i] == qArr[i]:
                ans = pArr[i]
            else:
                break
        return ans
