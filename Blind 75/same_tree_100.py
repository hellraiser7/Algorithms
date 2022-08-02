from binarytree import Node

def isSameTree(p,q):
    # returns true if:
    # 1. values are equal and none of them is empty
    # 2. both of them are empty (None)
    # returns false if:
    # 1. One of them is None -- isSameTree(14, x)  where x is none
    # 2. Values are unequal after comparing
    
    if not p and not q:
        # both None
        return True
    if not p or not q:
        # one of them is None, since we already checked both are none or not
        # if we get to this pt, it means at least one of p/q was none
        return False
    if p.val == q.val:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    return False # last case

if __name__ == "__main__":
    p = Node(4)
    p.left = Node(2)
    p.right = Node(7)
    p.left.left = Node(1)
    p.left.right = Node(3)
    p.right.left = Node(6)
    p.right.right = Node(9)

    q = Node(4)
    q.left = Node(2)
    q.right = Node(7)
    q.left.left = Node(1)
    q.left.right = Node(3)
    q.right.left = Node(6)
    q.right.right = Node(10)

    print("p is: ", p)
    print("q is: ", q)
    print("Is same tree? ", isSameTree(p,q))