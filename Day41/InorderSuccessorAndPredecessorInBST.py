# Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# traversal to find predecessor and successor
def preorder(root, key, pre, suc):
    if root is None:
        return

    if root.data < key and (pre[0] is None or pre[0].data < root.data):
        pre[0] = root

    if root.data > key and (suc[0] is None or suc[0].data > root.data):
        suc[0] = root

    preorder(root.left, key, pre, suc)
    preorder(root.right, key, pre, suc)

# return list with predecessor at index 0 and successor at index 1
def findPreSuc(root, key):
    pre = [None]
    suc = [None]
    preorder(root, key, pre, suc)
    return [pre[0], suc[0]]

if __name__ == "__main__":
    
    # Create BST:
    #      50 
    #     /  \
    #   30     70
    #   / \    / \
    # 20  40  60  80
    key = 65
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    
    result = findPreSuc(root, key)
    pre = result[0]
    suc = result[1]
    
    print((str(pre.data) if pre else "NULL"), (str(suc.data) if suc else "NULL"))