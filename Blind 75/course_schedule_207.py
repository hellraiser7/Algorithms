from collections import defaultdict

def canFinish(numCourses, prerequisites):
    # we will be able to finish the courses if there is no cycle in the graph
    # for e.g.: prereq = [[0,1],[1,2],[2,3],[3,4]], 0 is dependent on 1, 1 on 2, 2 on 3 and 3 on 4
    # So 4 is the first course you need to complete in order to finish all of them
    # 0 -> 1 -> 2 -> 3 -> 4. No cycle, hence canFinish() returns True
    # For 0->1->2->3->4
    #     ^           |
    #     |           |
    #     ------------- 
    # 4 connected to 0, we have a cycle, which means we need to complete 0 before 4, which is not possible
    # So canFinish returns False
    # First convert the list into a defaultdict graph
    visited = [False] * numCourses
    graph = createGraph(defaultdict(list), prerequisites)
    # we got the graph, now do DFS and check for cycle
    # currentPath is required to store the currently visited nodes
    # cycle is present if the currentNode is present in the current DFS path
    # pop from here when encountering a leaf node, to backtrack to next neighbor
    currentPath = []
    for currentNode in range(numCourses):
        if not visited[currentNode]:
            if not DFS_Util(visited, graph, currentPath, currentNode):
                return False
    return True 

def createGraph(graph, prerequisites):
    for u,v in prerequisites:
        graph[u].append(v)
    return graph

def DFS_Util(visited, graph, currentPath, currentNode):
    visited[currentNode] = True
    currentPath.append(currentNode)
    for neighbor in graph[currentNode]:
        # check if not visited, perform DFS
        # else, check if in current_path, return False as cycle detected
        if not visited[neighbor]:
            if not DFS_Util(visited, graph, currentPath, neighbor):
                return False
        elif neighbor in currentPath:
                return False
    # for loop done, encounter a leaf node
    # remove currentNode from path, and return True for that specific path
    # we still have other paths to check
    currentPath.pop()
    return True
if __name__ == "__main__":
    numCourses = 5
    prerequisites = [[0,1],[1,2],[2,3],[3,4]]
    print(canFinish(numCourses, prerequisites))
