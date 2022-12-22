## Kosaraju Algorithm for SCCs

Steps in finding the SCCs and number of SCCs in KOSARAJU's algorithm:

1. Do DFS of graph and fill the stack in order of increasing finish times (like topological sort exactly). Do normal DFS, then after the for loop, append in stack
2. Create a transpose/reverse graph and make all vertices false, for the second phase of DFS
3. Do 2nd DFS, this time on transpose graph as we need to find the SCCs. 
4. Once we do DFS on transpose graph, we see that if we start a DFS in one SCC from any node, all other nodes in that SCC can be reached, but since it is a transpose graph, there is no outgoing node from one SCC to next (source becomes the sink now, only incoming arrows)
5. So to reach other SCC, we need to make a manual jump, hence we need to perform while (stack): and call DFS_Util from popped nodes of stack one by one if not visited
6. Once recursion finishes, we increment the counter. This is where we'll make the manual jump. This signifies that the current SCC is detected and we move on to the next by popping the next element in stack.
7. Return the count

Too many steps that go in detail but it was necessary.

## Tarjan Algorithm For SCCs

Steps in finding the SCCs and number of SCCs in TARJAN's:

1. Declare variabled low[] = lowest discovery time accessible for the current node, this array is variable, disc[] = discovery time of the current node, this array is fixed, as well as a timer initialized in init function as 0.
2. Declare visited stack to keep track of visited order, and SCC_componentsList that stores all SCCs in a list of lists
3. Go through all vertices in main program, and call the util function if vertex not discovered.
4. In util function, change low[currentNode] = timer = disc[currentNode], and increment timer. Also append currentNode in visited stack.
5. Go through its neighbors, if neighbor not discovered, recurse normally (DFS). After backtracking and coming back to this, we perform low[currentNode] = min(low[currentNode],low[neighbor]), and then on to the next neighbor, we take low[neighbor] since after backtracking, we already know the future subgraphs emanating from the currentNode, hence we can make a decision that way.
6. In elif, we check if neighbor is in visited, if so, there is a back edge since a cycle is created (thats why node is still in visited), so perform:
low[currentNode] = min(low[currentNode], disc[neighbor]). We take disc[neighbor] because it is a back edge, and we do not know the future values or other node edges of neighbor as it is like a parent. We only know the disc value since that is constant after discovering the node.
7. If control doesnt go towards elif, it means we have a cross edge. And we don't process cross edges because it is of no use. To process cross edges, it would mean that we have to move inside what could likely be another SCC and it gives us a wrong set of nodes for an SCC. Hence it doesn't yield any SCC related info.
8. After processing all neighbors, declare a SCC_nodes list as empty, and check if low[currentNode] == disc[currentNode]. This would mean that the currentNode is a head node, and the SCC will stop at that node. So, run a while loop until we encounter the current head node and put it in the SCC_nodes[]. Also, put the SCC_nodes[] inside the SCC_componentsList
9. Return SCC_componentsList from the main program.
Below is the dry run and somewhat legible recursion tree for future reference. No need to dry run like this again. Just remember the main steps. Code isn't that heavy.
![Tarjan_recursion_tree](https://user-images.githubusercontent.com/51331982/208999715-c43b0ba7-6bf5-4b53-b3a1-1cc9ca499710.png)

### Articulation Points using Tarjan's algorithm

An AP is a node when removed from the graph, breaks the graph into multiple components (single point of failure in a network)

Steps to find APs

1. Maintain a parent[] array where parent[u] stores the parent of node u
2. Do the same as tarjans, declare disc[], low[], timer = 0 initially and an APlist to store the nodes that are APs
3. For each vertex, call the helper Util func, in the helper, low[curr] = timer = disc[timer], timer++, just like the tarjansSCC done above.
4. No need for a visited set since we do not need a topological sorting order, just need to find the APs
5. In helper, go through the neighbors of currentNode, if not yet discovered, inc no. of children by 1, then recurse for the neighbor
6. After recursion statement, when DFS process backtracks, do the same as tarjanSCC. low[cur] = min(low[cur], low[neigh]) and check first case of AP: if currentNode is a root node (parent[curr] == -1) and it has two more children, if so, append in APList
7. Second case: if currentNode is not root, and low[neighbor] >= disc[currentNode], it will be an AP. Meaning: we check for any backedges from subgraph v of u, towards ancestor of u. If there is one, that would mean the low value of neighbor will modify to something lower than disc value of its parent, hence the no. of components will not increase in that case, so to avoid backedge, the inequality is given. Append in APList if true
8. In elif statement (same level as the first "if" check for undiscovered neighbor), check if theres no backedge from parent to neighbor. If neighbor happens to be immediate parent of currentNode, then we ignore that case because we assume to be removing the currentNode for checking AP. So the backedge to parent actually doesnt exist at the moment. So on true, do same as tarjansSCC point 6.
9. Return APList from main program.
