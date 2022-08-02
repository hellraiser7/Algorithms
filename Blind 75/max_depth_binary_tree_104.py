from binarytree import Node

def maxDepth(root):
    if root:
        return (1 + max(maxDepth(root.left), maxDepth(root.right)))
    return 0
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(9)

    print("The tree is: ", root)
    print("The maximum depth is: ",maxDepth(root))