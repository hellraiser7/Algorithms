from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    # fill the stack that contains the nodes in increasing order of finish times
    # that is, the nodes without any outgoing arrows (leafs) will finish processing first
    # First Phase of DFS
    def fillOrder(self, visited, node, finishTimes):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.fillOrder(visited, neighbor, finishTimes)
        finishTimes.append(node)
    
    # Second Phase DFS (transpose graph)
    def DFS_Util(self, visited, node):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.DFS_Util(visited, neighbor)
    
    def Transpose(self):
        transposeGraph = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                # Edge (u->v)
                transposeGraph.addEdge(v,u)
        return transposeGraph

    # Main function to find and count the number of SCCs
    def SCC(self):
        # Step 1: Do DFS in original graph and fill the stack
        visited = [False]*self.V
        finishTimes = []
        count = 0
        for node in range(self.V):
            if not visited[node]:
                self.fillOrder(visited, node, finishTimes)
        # Step 2: Create a transpose graph from the original
        transposeGraph = self.Transpose()
        # Step 3: Explore the transpose graph now with DFS_Util, with popped values of stack
        # Which means start with the nodes with higher finish times
        visited = [False]*self.V
        while finishTimes:
            node = finishTimes.pop()
            if not visited[node]:
                transposeGraph.DFS_Util(visited, node)
                count += 1
            #Once recursion ends for one i, we know that the SCC ends,
            #Now we are in for a different SCC, and the previous one ended.
            #Hence to count the number of SCCs, we need a counter
        return count

if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(4,7)
    g.addEdge(5,6)
    g.addEdge(6,4)
    g.addEdge(6,7)
    print(g.SCC())   



        