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
