from binarytree import Node
from collections import deque

def levelOrder(root):
    # use a deque
    q = deque()
    result = []
    if root:
        q.append(root)
    while q:
        siblingValues = []
        p = q
        for i in range(len(p)):
            # popleft - append in siblingValues - check its children and append in q
            node = q.popleft()
            siblingValues.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # append all siblingVal in result
        result.append(siblingValues)
    return result

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(1)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print("Level Order Traversal: ", levelOrder(root))

