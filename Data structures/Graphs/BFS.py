from collections import defaultdict, deque

class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def BFS(self, v):
        visited = set()
        queue = deque([])
        visited.add(v)
        queue.append(v)
        return self.BFS_Util(visited, v, [], queue)
    
    def BFS_Util(self, visited, v, result, queue):
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.graph[node]:
                # check neighbors
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result
    
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
    # BFS
    print(G.BFS(2))

        

        