from operator import invert
from binarytree import Node

def invertTree(root):
    if not root:
        return None
    # now swap the children
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(9)

    print("The inorder traversal of tree is: ", root)
    print("The inorder traversal of the inverted tree is: ", invertTree(root))