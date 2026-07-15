# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            # case 1 niche he mil gya
            nicheHeMilGya = left + right + root.val
            # case 2 root k saath ya yeleft side ya riht
            koiEkAccha = max(left, right) + root.val
            # case 3 keval root badhiya hai
            onlyRoot = root.val
            self.maxi = max(self.maxi, nicheHeMilGya, koiEkAccha, onlyRoot)
            return max(koiEkAccha, onlyRoot)

        self.maxi = -float("inf")
        solve(root)
        return self.maxi
