"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = defaultdict()
        def dfs(node):
            if node in oldToNew:
                # if already present
                return oldToNew[node]
            # create deep copy
            deepCopy = Node(node.val)
            # link in hashmap
            oldToNew[node] = deepCopy
            for neighbor in node.neighbors:
                # for each neighbor of current node,
                # create a deep copy
                deepCopy.neighbors.append(dfs(neighbor))
            return deepCopy
        if node:
            # if node exists
            return dfs(node)
        else:
            return None