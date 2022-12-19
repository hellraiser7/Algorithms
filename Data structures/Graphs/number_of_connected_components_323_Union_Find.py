from collections import deque, defaultdict

class Graph:
    def __init__(self, V):
        self.V = V    
    #directed graph
    
    # parent array has all -1. If a node is the ultimate parent, then it's value will be -1
    # since it won't have any ancestors (it is the one true ancestor of every node in that component)
    def findParent(self, parent, i):
        if parent[i] < 0:
            return i
        return self.findParent(parent, parent[i])
    
    # Union
    def Union(self, components):
        parent = [-1]*self.V
        rank = [0]*self.V
        count = 0
        for edge in components:
            # [[0,1],[1,2],[3,4]]
            u, v = edge[0], edge[1]
            # find parent of both nodes, and depending on the value, attach the nodes
            u_parent = self.findParent(parent, u)
            v_parent = self.findParent(parent, v)
            print(u_parent, v_parent)
            if rank[u_parent] > rank[v_parent]:
                parent[v_parent] = u_parent
                # rank array is unmodified
            elif rank[u_parent] < rank[v_parent]:
                # attach u_parent to v_parent
                parent[u_parent] = v_parent
            else:
                # merge and update rank if both nodes at same rank
                parent[u_parent] = v_parent
                rank[v_parent] += 1
            print(parent, rank)
        for i in parent:
            if i == -1:
                count += 1
        return count
    
if __name__ == "__main__":
    G = Graph(5)
    components = [[0,1],[1,2],[3,4],[2,3]]
    print(G.Union(components))

        


            
    