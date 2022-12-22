from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.timer = 0
    
    # undirected    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bridges(self):
        # same as articulation points, we don't need visited set
        disc = [-1]*self.V
        low = [-1]*self.V
        parent = [-1]*self.V
        bridges = []
        for node in range(self.V):
            if disc[node] == -1:
                # undiscovered
                self.bridges_Util(disc, low, node, parent, bridges)
        return bridges
    
    def bridges_Util(self, disc, low, currentNode, parent, bridgesList):
        # Step 1: disc, low, and timer, no need of visited set
        disc[currentNode] = self.timer
        low[currentNode] = self.timer
        self.timer += 1
        for neighbor in self.graph[currentNode]:
            # Step 2: If undiscovered, update the parent array and recurse
            if disc[neighbor] == -1:
                parent[neighbor] = currentNode
                self.bridges_Util(disc, low, neighbor, parent, bridgesList)
                # after recursion, backtracking like tarjans
                low[currentNode] = min(low[currentNode], low[neighbor])
            # Step 3: Check if it is a backedge to one of the ancestors of current
            # If it is, then it is not a bridge
                if low[neighbor] > disc[currentNode]:
                    bridgesList.append([currentNode, neighbor])
            # backedge to one of ancestors that is not the parent, we alter the low value
            if neighbor != parent[currentNode]:
                low[currentNode] = min(low[currentNode], disc[neighbor])

if __name__ == "__main__":
    G = Graph(5)
    G.addEdge(0,1)
    G.addEdge(0,2)
    G.addEdge(1,2)
    G.addEdge(0,3)
    G.addEdge(3,4)
    print(G.bridges())

            
        
    