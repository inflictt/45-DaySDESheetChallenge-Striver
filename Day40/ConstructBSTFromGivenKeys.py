# Python program to find all binary
# trees from 1 to n
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to construct all possible
# binary trees 
def get_trees(start, end):
    trees = []

    # Base case: If start index is greater than end, 
    # return empty tree (None)
    if start > end:
        trees.append(None)
        return trees

    # Iterate through all values in the array and 
    # construct left and right subtrees
    for i in range(start, end + 1):
        
        # Generate all left subtrees
        left_trees = get_trees(start, i - 1)

        # Generate all right subtrees
        right_trees = get_trees(i + 1, end)

        # Combine each left and right subtree 
        # with the current root
        for left in left_trees:
            for right in right_trees:
                
                # Make i as root
                root = Node(i)
                root.left = left
                root.right = right

                # Add the constructed tree to 
                # the list of trees
                trees.append(root)

    return trees

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

if __name__ == "__main__":
    trees = get_trees(1, 3)

    for tree in trees:
        preorder(tree)
        print()