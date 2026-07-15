# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,path,main):
        if not root:
            return 
        if len(path)==0:
            path+=str(root.val)
        else:
            path+="->"
            path+=str(root.val)
        self.dfs(root.left,path,main)
        self.dfs(root.right,path,main)
        if not root.left and not root.right:
            main.append(path)
        return main
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = self.dfs(root,"",[])
        return ans
        # algo made path as string so whenever new visits made of same side path ican add vals with arrow to it if it has no exisitng path vals in it if it is empty then ill start with value only
        # breaking path case when we know that we cant go either left or right so dead end thats the point we break and return main so it fall backs and to the root and starts itr other side .