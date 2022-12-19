from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DFS(self):
        visited = [False]*self.V
        number_of_connected_components = 0
        for node in self.graph:
            if not visited[node]:
                self.DFS_Util(visited, node)
                # increment the count after each DFS process
                number_of_connected_components += 1
        return number_of_connected_components
    
    def DFS_Util(self,visited, node):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.DFS_Util(visited, neighbor)
    
if __name__ == "__main__":
    G = Graph(10)
    G.addEdge(0,1)
    G.addEdge(1,2)
    G.addEdge(3,4)
    G.addEdge(5,6)
    G.addEdge(6,7)
    G.addEdge(7,5)
    G.addEdge(8,9)
    print(G.DFS())
            

            