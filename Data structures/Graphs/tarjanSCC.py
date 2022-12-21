from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.timer = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # main function that will call the recursive function
    def tarjan(self):
        # Declare global variables for visited stack, low and discovery lists
        visited = []
        low = [-1]*self.V
        disc = [-1]*self.V
        SCC_componentsList = []
        for vertex in range(self.V):
            if disc[vertex] == -1:
                self.tarjan_Util(visited, vertex, low, disc, SCC_componentsList)
        return SCC_componentsList
        
    def tarjan_Util(self, visited, currentNode, low, disc, SCC_componentsList):
        # Step 1: Append current node in visited, and increment low, disc, update timer
        visited.append(currentNode)
        low[currentNode] = self.timer
        disc[currentNode] = self.timer
        self.timer += 1
        # Step 2: Go through every neighbor, change low value depending on normal backtrack or backedge
        # if neighbor is undiscovered, then do the normal DFS recursion
        # if already discovered, it means it is a cross edge or a back edge
        # Now, if the node is in visited stack (not popped out yet), it means, it is a back edge
        # If not in visited stack either, then it's a cross edge, and we don't do anything
        for neighbor in self.graph[currentNode]:
            # if not discovered, recurse
            if disc[neighbor] == -1:
                self.tarjan_Util(visited, neighbor, low, disc, SCC_componentsList)
                # comes here after the current DFS process finished and now its backtracking
                # change low value, since now we know the future low values, so we know the current node
                # can reach some future nodes
                low[currentNode] = min(low[currentNode], low[neighbor])
            # if discovered, we need to check its availability in visited stack
            # it will be a back edge if the neighbor exists in stack, because
            # there is a cycle formed back to the parent
            # taking disc[neighbor] because we only know the fixed discovery times of the neighbor
            # and have no idea about their low times, which can be variable depending on other back edges
            if neighbor in visited:
                low[currentNode] = min(low[currentNode], disc[neighbor])
        
        # After going through all neighbors (no outgoing arrows), print the SCCs if head node is found
        # Pop stack till current Node is reached
        SCC_nodes = []
        if low[currentNode] == disc[currentNode]:
            while (visited[-1] != currentNode):
                SCC_nodes.append(visited[-1])
                visited.pop()
            # currentNode to still be popped
            SCC_nodes.append(visited[-1])
            visited.pop()
            SCC_componentsList.append((SCC_nodes)) # sorting not necessary

if __name__ == "__main__":
    G = Graph(7)
    G.addEdge(0,1)
    G.addEdge(1,2)
    G.addEdge(1,3)
    G.addEdge(3,4)
    G.addEdge(4,0)
    G.addEdge(4,5)
    G.addEdge(5,6)
    G.addEdge(6,5)
    G.addEdge(4,6)
    print(G.tarjan())

            