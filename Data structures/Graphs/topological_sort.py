from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def topologicalSort(self):
        visited = [False]*self.V
        stack = [] # to store the finishing times, higher finish times -> nodes at the top
        for node in range(self.V):
            if not visited[node]:
                self.topologicalSort_Util(visited, node, stack)
        return stack[::-1] # print reverse for topological order
    
    def topologicalSort_Util(self, visited, node, finishTimes):
        visited[node] = True
        # visit the node, then do DFS for its neighbors
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.topologicalSort_Util(visited, neighbor, finishTimes)
        # on reaching leaf nodes, we have completed our current DFS path
        # on doing so, we push the node into the stack
        finishTimes.append(node)

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
  
    print(g.topologicalSort())
            