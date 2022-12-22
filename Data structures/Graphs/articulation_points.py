from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.timer = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def find_articulation_points(self):
        visited = set()
        disc = [-1]*self.V
        low = [-1]*self.V
        parent = [-1]*self.V # store parents of respective nodes
        articulationPointsList = set()
        for node in range(self.V):
            # not discovered
            if (disc[node] == -1):
                self.articulation_points_Util(disc, low, visited, parent, node, articulationPointsList)
        print(list(articulationPointsList))

    
    def articulation_points_Util(self, disc, low, visited, parent, currentNode, AP):
        # Step 1: Append in visited set, fill low[currentNode], disc[currentNode] with timer and increment timer
        # Same as tarjan's algorithm
        visited.add(currentNode)
        disc[currentNode] = self.timer
        low[currentNode] = self.timer
        self.timer += 1
        children = 0
        # Step 2: Iterate through all neighbors of current
        # If not discovered, then update parent[neighbor] and do dfs on neighbor
        for neighbor in self.graph[currentNode]:
            if disc[neighbor] == -1:
                # neighbor not discovered
                parent[neighbor] = currentNode
                children += 1
                self.articulation_points_Util(disc, low, visited, parent, neighbor, AP)
                # Step 3: After recursion of currentNode is done and it backtracks, it comes to this line
                # Same as tarjanSCC, we modify the low value of currentNode since we now have knowledge of its future values
                low[currentNode] = min(low[currentNode], low[neighbor])
                # Step 4: Check for Case 1, i.e., if currentNode is a root and it has two or more children, then it is an AP
                if parent[currentNode] == -1 and children >= 2:
                    # append AP in list
                    AP.add(currentNode)
                # Step 5: Check for Case 2, i.e., if currentNode is not a root and there's no backedge from its subgraph to one of its ancestors
                elif parent[currentNode] != -1 and low[neighbor] >= disc[currentNode]:
                    AP.add(currentNode)
            # in elif case, we have to take minimum of low val of current and disc of neighbor, just like tarjanSCC
            # but it shouldn't be a backedge to it's own parent, otherwise it will be null and void, as we pretend to remove currentNode along with its back/cross/normal edges
            elif parent[currentNode] != neighbor:
                low[currentNode] = min(low[currentNode], disc[neighbor])

if __name__ == "__main__":
    G = Graph(6)
    G.addEdge(0,3)
    G.addEdge(3,5)
    G.addEdge(3,4)
    G.addEdge(0,2)
    G.addEdge(0,1)
    G.addEdge(1,2)

    g3 = Graph(7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    G.find_articulation_points()
    g3.find_articulation_points()