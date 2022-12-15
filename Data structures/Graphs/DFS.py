# here goes nothing
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        # undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS_Util(self, visited, v, result):
        visited.add(v) # mark current node visited
        result.append(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFS_Util(visited, neighbor, result)
        return result
    
    # need to separate the main caller from the recursive function because
    # there could be multiple connected circuits in a graph (lone nodes or multiple SCCs)
    def DFS(self, v):
        visited = set()
        result = []
        return self.DFS_Util(visited, v, result)

if __name__ == "__main__":
    G = Graph(12)
    G.add_edge(0,1)
    G.add_edge(1,8)
    G.add_edge(8,9)
    G.add_edge(0,9)
    G.add_edge(8,7)
    G.add_edge(7,10)
    G.add_edge(10,11)
    G.add_edge(11,7)
    G.add_edge(7,6)
    G.add_edge(6,5)
    G.add_edge(5,3)
    G.add_edge(3,4)
    G.add_edge(3,2)
    G.add_edge(3,7)
    # DFS
    print(G.DFS(0))
