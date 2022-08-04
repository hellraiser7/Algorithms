from binarytree import Node

def getLowestCommonAncestor(root, p, q):
    # BST: check whether p and q are lesser/greater than root
    # if both lesser than root, recurse for the left half of tree, else right half
    # if one is in the left, other in the right, we get a split
    # and this split tells us that the LCA can be only the root and nothing else
    # 1. p and q greater than root
    if (p.val > root.val and q.val > root.val):
        return getLowestCommonAncestor(root.right, p, q)
    # 2. p and q lesser than root
    if (p.val < root.val and q.val < root.val):
        return getLowestCommonAncestor(root.left, p , q)
    # 3. Split
    return root

if __name__ == "__main__":
    llist = Node(4)
    llist.left = Node(2)
    llist.right = Node(7)
    llist.left.left = Node(1)
    llist.left.right = Node(3)
    llist.right.left = Node(6)
    llist.right.right = Node(9)

    p = Node(1)
    q = Node(3)

    print("p is: ", p)
    print("q is: ", q)
    print("The lowest common ancestor is: ", getLowestCommonAncestor(llist, p, q))
