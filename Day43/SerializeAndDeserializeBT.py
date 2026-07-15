
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ans = []
        def preorder(node):
            if not node:
                ans.append("#")
                return

            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        values = data.split(",")
        self.idx = 0

        def build():
            if values[self.idx] == "#":
                self.idx += 1
                return None

            node = TreeNode(int(values[self.idx]))
            self.idx += 1
            node.left = build()
            node.right = build()
            return node
        return build()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
