from same_tree_100 import *
from binarytree import Node

def isSubtree(root, subRoot):
    # use the logic of sametree
    # edge cases: 
    # 1. If subtree is null, it will always be a valid subtree
    # 2. If main tree is null, then return False
    # 3. If both null, true
    if not subRoot:
        return True
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

if __name__ == "__main__":
    p = Node(4)
    p.left = Node(2)
    p.right = Node(7)
    p.left.left = Node(1)
    p.left.right = Node(3)
    p.right.left = Node(6)
    p.right.right = Node(9)

    q = Node(7)
    q.left = Node(6)
    q.right = Node(9)

    print("p is: ", p)
    print("q is: ", q)
    print("Is subtree? ", isSubtree(p,q))