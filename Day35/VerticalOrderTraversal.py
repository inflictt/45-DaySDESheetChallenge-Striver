# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # main dfs call at 0 ,0. and like col ,level thing it is
        # idea -hashmap = {# col : [(row, value), (row, value), ...]}
        # dfs(node.left, row+1, col-1) #left 
        # dfs(node.right, row+1, col+1) #rigth thng
        def dfs(root, row, col):
            if not root:
                return
            if col not in hashmap:
                hashmap[col] = []
            hashmap[col].append((row, root.val))
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)

        hashmap = {}
        dfs(root, 0, 0)
        final = []
        for col in sorted(hashmap):
            hashmap[col].sort()
            temp = []
            for row, value in hashmap[col]:
                temp.append(value)
            final.append(temp)
        return final