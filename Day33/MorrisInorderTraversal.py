# Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    res = []
    curr = root

    while curr is not None:
        if curr.left is None:

            # If no left child, visit this node 
            # and go right
            res.append(curr.data)
            curr = curr.right
        else:

            # Find the inorder predecessor of curr
            prev = curr.left
            while prev.right is not None \
            and prev.right != curr:
                prev = prev.right

            # Make curr the right child of its 
            # inorder predecessor
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:

                # Revert the changes made in the 
                # tree structure
                prev.right = None
                res.append(curr.data)
                curr = curr.right

    return res


if __name__ == "__main__":
  
    # Representation of input binary tree:
    #           1
    #          / \
    #         2   3
    #        / \  
    #       4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    res = inOrder(root)
    
    for data in res:
        print(data, end=" ")