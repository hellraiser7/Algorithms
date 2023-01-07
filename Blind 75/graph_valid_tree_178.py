# check if there is no cycle and all components are connected to each other
# then only it will be a valid tree
from collections import defaultdict
def valid_tree(n, edges):
    # Step 1: Make the adjacency list from the edges given
    if not n:
        # null graph is always a valid tree
        return True
    adjacencyList = { i : [] for i in range(n)}
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    visited = set()
    # Step 2: Do DFS and if currentNode is not a backedge to previous, we recurse
    def DFS_Util(currentNode, previousNode):
        if currentNode in visited:
            return False
        # if not in visited, we iterate through its neighbors and recurse
        visited.add(currentNode)
        for neighbor in adjacencyList[currentNode]:
            if neighbor == previousNode:
                # if equal to previousNode, we have a false positive
                # 0 <--> 1 a back edge needs to be ignored
                continue
            # now handle the false case:  Step 4
            if not DFS_Util(neighbor, currentNode):
                return False
        return True
    # Step 5: Handle the second condition as well where the number of nodes when equal to visited set, we have one single component
    return DFS_Util(0,-1) and (len(visited) == n)

if __name__ == "__main__":
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]
    print(valid_tree(n, edges))








    
