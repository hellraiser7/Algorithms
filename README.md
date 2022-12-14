# Algorithms
Thought I could share my preparation, as staggered as it may be, on this platform so that I could even get the tiniest amount of confidence by sharing my solutions from solving leetcode.

## Blind 75
Problems solved (updated everyday ... kinda)

### Easy Leetcode

### 1. Best time to buy and sell stock (I) - Leetcode 121
 - Brute Force: O(n^2) time | O(1) space
   - Iterate with two for loops, keep tracking the bestProfit value for all pairs, at the end return the bestProfit
 - Optimized: O(n) time | O(1) space
   - Iterate with only one for loop through the array: keep tracking the current minimum. 
   - For e.g.: If arr = [7,1,3,5,6,4], bestProfit is 5 (day 2 buy, day 5 sell)
     - then currentMin is first element of array initially, then once we find a number lesser than that, change it to that number. Start loop from index 1, Carry out the        prices[i] - currentMin and calc bestProfit.
 
### 2. Valid Parentheses - Leetcode 20
   - Stack question (not intuitive from the get go)
   - Notice that the string must start from an opening bracket. 
   - Once an opening bracket is encoutered, the validity check will keep on going, until it finally encounters a closing one, then it needs to validate:
     - Keep appending into the stack if we keep encountering an opening bracket (storing the brackets in a hashmap will benefit us greatly with key as closing bracket)
     - compare TOS with current closing bracket, return false if not matching
   - Time: O(n) | Space: O(1) , well we needed a hashmap to store the bracket_map
   
### 3. Reverse a linked list - Leetcode 206
  - 3 pointers needed: previous, current and next: none, head, none
  - while current is not empty, these steps need to be followed:
    - next is current->next since we need to save nextNode first before manipulating pointers OW the next element is lost
    - reversing logic aka current->next = previous
    - now shifting the pointers: previous = current, current = next
    - After first iteration, the llist becomes something like: 1 -> 2 -> 3 -> 4 -> x  (prev at 2, next,current at 3)
### 4. Merge two sorted linked lists - Leetcode 21
  - 3 pointers again: current, A and B. A and B point to the next elements (from first and second llist) that need to be compared in order to find the next element in     the super linked list
  - 2 components: get the starting node, depending on whichever is smaller (A.head or B.head) and assign current to it, either inc A or B
  - Below is a rough sketch of the dry run that I'd conducted
  ![merge_two_sorted_lists_21](https://user-images.githubusercontent.com/51331982/182046844-3f7f5ed7-17af-4764-b4ac-f7f5cbe690b4.jpg)
  - A is smaller, so inc A.
    - A is at 3, B at 2, so current points to B, and current shifts to B before B=B->next happens
    - Similarly, in the next itr, A at 3 compared to B at 4 now. And A is smaller, so current points to A, shifts to A before A = A.next happens
    - Any one of those 2 llists is empty, then we break and connect the current pointer to the list that's not empty. 
  - Time: O(m+n) | Space: O(1) 

### 5. Linked List Cycle - Leetcode 141
  - Probably the simplest of the lot.
  - Iterate through the entire llist, and store the nodeAddresses inside a set.
  - If at any time, we encounter a nodeAddress already existing within the set (next ptr pointing towards this node), we know that it contains a cycle
  - No other corner case.
  - Time: O(n) | Space: O(n)
 
### 6. Invert Binary Tree - Leetcode 226
  - Simple recursion, although I need to keep revising in order to stand a chance at understanding complex recursion problems
  - At the root, go left and go right, swap the children and recurse on both halves of the tree. Return root
  - Time: O(n) where n is the number of nodes in the tree

### 7. Maximum Depth Binary Tree - Leetcode 104
  - Simple recursion
  - Check if root exists, if it does, add 1 to the max depth from both left and right halves 
    - return (1+max(maxDepth(root.left),maxDepth(root.right)))
    - else return 0 depth
  - Time: O(n) where n is the number of nodes in the tree
  - A dry run of the recursion: 
  ![max_Depth_binary_tree_104](https://user-images.githubusercontent.com/51331982/182285190-7920cbc4-252f-4c3e-8600-a9a1bce08558.jpg)

### 8. Same Tree - Leetcode 100
  - Simple Recursion
  - Equality of nodes will exist when:
    - p.val == q.val and none of them is empty, in which case we put the recursion call of sametree(p.left,q.left) and sametree(p.right, q.right)
    - Both p and q are none, hence they are equal
  - Unequality:
    - One of p or q is None
    - If both p and q have non empty vals, p.val != q.val

### 9. Subtree of another tree - Leetcode 572
  - Not so simple, but depends on the previous problem
  - Use same tree logic
  - Check for each node of the main tree, if it's equal to the subtree
  - The same process for checking SameTree continues, the only difference being that this happens for every node
  - Time: O(T) | Space: O(1) where T = number of nodes in the subtree

### 10. Lowest Ancestor of a Binary Search Tree - Leetcode 235
  - Use the concept of a binary tree in order to lower the time complexity.
  - Can use both iterative as well as recursive solutions
  - LCA cases: 
    - If anywhere, p and q are in the opposite sides of a tree, then the root will be the LCA ( one is greater than root, the other is lesser), return root in this case
    - If both are smaller or greater than the root, then we recurse towards either the left half of tree or right, since it is a BST (2 if statements: if p.val > root.val and q.val > root.val -> return LCA(root.right, p,q), and the other one for handling the smaller than root case, where we go left
    - Time: O(1) with iterative approach, can go upto O(n) in recursion due to the stack | O(1) space
    
    ![LCA](https://user-images.githubusercontent.com/51331982/182887723-76f820e5-87da-4145-9894-56d7c9be3bce.jpeg)
### 11. Climbing Stairs - Leetcode 70
  - Calculate recurrence relation first. Start with 1 step, 2 steps then 3
  - See a pattern emerging.
  - Can be solved dynamically or recursively
  - Time: O(n) | Space: O(n) for iterative approach, O(1) for recursive

### 12. Meeting Rooms - Lintcode 920
  - This is a premium leetcode question. Since I am poor, gonna do it in lintcode instead (free site)
  - Sort by start times since we need the end time perspectives here.
  - We can attend the meetings if end time of one meeting is smaller or equal to the start time of the next meeting, after sorting.
  - Time: O(nlogn + n) = O(nlogn) since sorting takes nlogn time and then the pass through the intervals array | Space: O(1)
  - e<sub>i</sub> <= s<sub>i+1</sub>
### 13. Number of 1 Bits - Leetcode 191
  - While n is not zero, do modulus with 2, to get the MSB. (Modulus with 2 means getting whether the current number is odd or even, so we get the MSB)
  - If MSB == 1, then inc sum, and right shift n.
  - Genius approach would be to do n = n & (n-1) since this reduces the Time complexity to only have no.of iterations = no. of set bits. 
  - As we do & with previous number, we eliminate each set bit one by one. So, if there are only a few, it helps us rather than go all the way 32 times.
  - Do a DRY again!
  - Time: O(32) or less | O(1) Space
### 14. Counting bits - Leetcode 338
  - Use the same above logic, for each n, do getSetBits as done above
  - Or we can do it in one pass, without the extra O(32) going inside the for loop
    - in one pass, keep a dp table with n entries of zeros first. then keep on appending it. Dividing by 2 is equivalent to right shifting
    - ans[i] = ans[i//2] + i%2
    - Get the MSB bit whether 1 or 0, then get the no. of set bits value from the number without the MSB, which is the right shifted value
  - Time: <O(32) | Space: O(1)

### 15. Reverse Bits  - Leetcode 190
  - Can convert int to binary first, starting from 2nd index since the number will be "0b1011..."
    - Reverse the binary string, then if length of that reversed string is lesser than 32, add zeros at the end to fill it up till length of 32
    - Time: O(n) for reversing or slightly lesser due to python being python | Space: O(1)
  - Can also do modulus with 2, get the MSB and push it into a new string. Then right shift the number by 1, continue till it becomes zero
  - Handle the 32 length scenario as mentioned above, and thats about it
  - Time: O(n) | Space: O(n)

### 16. Missing Number - Leetcode 268
  - Sort the array in ascending order.
    - check if there's an arr[i] != i, return that i
    - no false returns, always a happy solution exists
    - This is O(nlogn) time, O(1) space. We can do better
  - To do better, we can calculate the natural number sum till the length of array nums *n* = n(n+1)/2
    - Calculate the actual sum of elements, and then subtract both to get the missing number
    - Sweet, ain't it? 
    - (I'm seriously bragging about finding this solution on my own lol)
    - This gets us Time: O(n), Space: O(1). In python, the sum(nums) method can be lesser than O(n)

### Medium Leetcode

### 17. Group Anagrams - Leetcode 49
  - Think how to calculate all permutations of a string
  - Calculate them for one string, then check if other strings exist in that permutations list
  - Not necessarily a solution we can code, since it gets to exponential.
   - One thing we can do is sort each string inside the array first, and check how many of them are equal after all the elements are sorted
   - In place sorting could be done
   - Push into a new output list of lists
   - Time: O(m.nlogn) if m = length of array, n = length of each string | Space: O(m) 
  - Optimized solution:
   - Use a hashmap!!
   - Keep a list arr = [0]*26 for the 26 alphabets
   - For each element in the input, and for each char in each str, calculate the frequency of each char
   - then append into defaultdict with the tuple as key (since the key needs to be immutable). If keys are same (anagrams), the values will get clubbed into an array
   - Time: O(26mn) = O(mn) since 26 is constant | Space: O(26) only a list for alphabet frequency counting is needed
   - For e.g: string 'abe'  will have the countArray = [1,1,0,0,1,0,0 ... 0] 26 values. It keeps count of frequency of each char in its respective position. 1st pos for a, 26th pos for z

### 18. Top K Frequent Elements - Leetcode 347
  - First solution: sort the array with respect to count of elements (use sorted function, with key = list.count, reverse = true)
    - We get the list sorted wrt decreasing frequency
    - iterate through the sorted list and only return first k element array once all k elements have been encountered
    - Time: O(nlogn) | Space: O(k) since we need to store the k frequent elements in a new array and return it
  - Second solution: Hashmap? Everything boils down to a hashmap. The solution for world hunger is probably a hashmap.
    - Get the frequencies in a hashmap (key as array element, value as its frequency)
    - iterate from 0 to k (k frequent)
    - for each pass, go through the hashmap and find the key for which we get max value.
    - Then delete that key from hashmap, and store the corresponding array element with max frequency in a new result array
    - return the new array which will acquire O(k) space
    - Time: O(n + k*no.ofunique array elements) ~ O(n + k^2) lesser than nlogn | Space: O(k) for the resultant array

### 19. Product of Array but itself - Leetcode 238
  - First solution: can use division. Calculate product of all elements, and then divide by the current element to get the product in output array for current pos
    - Handle edge cases first before moving on to main logic: 1 zero means only one nonzero element in output in pos where zero is located, more than one zero means a zeroes list is returned
    - Time: O(n) | Space: O(n) for output array, but uses division
    - Need a solution without using division
  - Maybe iterating, popping the element, calculating the product, and then pushing it back in? TLE for this one.
    - Use prefix and postfix values in order to calculate the thing without division.
    - See out prefix product for every element, then calc postfix product (product of everything after that element) for the elements
    - First use prefix & postfix arrays, so space will be O(2n), then try eliminating the use of these arrays to limit space to O(1), ofcourse output array doesnt count towards space complexity.

### 20. Encode and Decode strings - Lintcode 659
  - Another premium question - encode a list of strings to a string
  - Use a delimiter along with the length of each individual string in order to store the list of strings into a string
  - So, ["we","love","lintcode"] => "2$we4$love8$lintcode" => ["we","love","lintcode"]
  - encoding is easy: append length of string and delimiter (any special character really, or anything else, covers all corner cases) to resultant string and return
  - decoding: use 2 pointers i and j. i for the outer loop, j to keep going in the inner one, till it encounters the "$", then get that char length, and append that char which will occur from str[i:j] since j+1 would be at "$". Then reinitialize i to next char start (j+1+length of current), and j = i, to start over
  - Time: O(n) for encoding, O(number_of_digits_in_length_integer * n) for decoding, where n = list of strings length
    - This is just an instance. If there are 200 chars in every string, there'll be 3 digits to traverse for inner loop, and times that of length of the list (say 200) which becomes O(3*200)
    - So in short, total design algorithm's time: O(n + l * n) ~ O(n)

### 21. Longest Consecutive Sequence - Leetcode 128
  - First solution: 
    - Sort the array
    - Once sorted, you can convert into set, reconvert to list to remove duplicate elements
    - Then iterate through entire unique list till penultimate
    - If numsSet[i+1]  == numsSet[i] + 1 (consecutive ones), then increment result
    - else, compare maxValues and store the latest max, reinitialize output to 1 for next sequence
    - Time: O(nlogn) | Space: O(n) or O(1) depending on whether we use a stack or not for maxValues
  - Second solution:
    - create a set from the list
    - Iterate through the numsSet
    - check if the current element is the starting of a sequence, (if ele - 1 not in numsSet), initialize length as 0
    - while loop inside for to go till the end of consecutive elements present in the set while ele + length in numsSet, do inc length
    - do maximum of local length and the maxValue
    - Time: O(n), Space: O(n) since we used a numsSet

### 22. 3Sum - Leetcode 15
  - First solution:
    - Brute Force tells us that we can check all possible triplets and then check how many of them add up to 0. We can even add checks for duplicates. This is an O(n^3) time solution.
  - Second solution:
    - Sort in ascending order.
    - Driving inspiration from 2 sum II. Please solve that first while revising.
    - Fix the first number, and then using left and right pointers, calculate the next two numbers in the candidate triplet. So, we'll need one main loop, inside which there must be a while loop to check while left < right
    - if threesum < 0 , increment left pointer, since the list is sorted, and once we increment, the sum will be bigger, and much closer to 0 than previously done
    - if threesum > 0, we've gone too far with the sum, hence right ptr needs to be decremented to get closer to the zero sum
    - if == 0, we got it. append triplet in output and another while is needed
    - left pointer needs to be incremented here, and a last **while** is needed since we can encounter duplicates in the left pointer too. In order to not go through the same left pointer again and again, we'll keep incrementing left pointer till we get a different number.
    - Once we increment left pointer and get a different number, we go through the logic again, and we see that the right ptr decrement will be taken care of in the next iterations, so only need to take care of left ptr
    - Revise again!!!!
    - Time: O(nlogn + n^2) since we go through the list at most twice with two loops, one outer one and other while l<r one. Space: O(1) since we use l and r ptrs.

### 23. Container with most water - Leetcode 11
  - First Solution:
    - Brute Force: Run two loops to find the candidate vertical pairs. One of them will give max Area, keep tracking this maxArea and return
      - O(n^2) time, O(1) space, gives TLE
  - Second solution: 
    - Two pointers again, but we need to get the logic as to how to increment/decrement those pointers
    - while left < right, get the current area with current l and r ptrs. Then if height at left ptr is smaller than that of right, increment left pointer since we need a bigger height in order to maximize area
    - We might/might not get a bigger height once we inc/dec, but still we need to keep checking like this throughout the list.
    - similarly, if height at right ptr is smaller, decrement right ptr.
    - keep track of maxArea.
    - Time: O(n) | Space: O(1)

### 24. Longest Substring Without Repeating Characters - Leetcode 3
  - First Solution:
    - Brute Force O(n^2). Find all possible substrings and then check if they have repeating characters. Keep tracking maxLength and return it. It may go towards O(n^3)
  - Second Solution:
    - Sliding Window with left and right
    - Use a set to keep the substring characters that have been encountered till current itr.
    - while inside a for loop, while loop to keep incrementing left pointer until we have eliminated the repeating character(s) out of the set so that we can start with the fresh substring with a fresh hashset collection and l & r ptrs
    - we keep inc. left pointer, and also removing that char at which left ptr sits, from the set, since we need to keep updating the substring window (window changes, and so does the set)
    - if the current char is not in hashset, add into set outside while loop
    - Time: O(n) since lookup time in set is O(1), worst case scenario would be O(2n) when there is a repeating char at end of string "abcdefghijklmnpp", then left ptr needs to go all the way towards the end, so twice traversal needed
    - Space: O(n) for hashset 

### 25. Longest Repeating Character Replacement - Leetcode 424
  - First Solution:
    - Sliding window using a hashmap for storing count of each uppercase character.
    - Need to calculate maximum frequency in current window defined by left and right ptrs as done in above questions
    - condition length_of_current_substring - maxFrequncy <= k, needs to be satisfied in order to find out whether the other chars in the current window can be replaced or not
    - If that number is lesser or equal to k, it means that all of the other characters can be replaced as k is the upper limit given.
    - If not equal, then we need to slide the left ptr one step ahead since the window will not be valid then. 
    - Shift the left ptr, decrement the count of the char where the left ptr was sitting, and do the procedure again.
    - Keep going till the end of the list
    - Time: O(26.n) | Space: O(26) for the alphabet hashmap
  - Second solution:
    - No need for the hashmap. Only need to keep track of maxFrequency and have some good logic on that.
    - Cannot come up with this in an interview. It's not possible. But good to know still.
    Here is the dry run for the example "AABABBA",k=2
    
    
  ![image](https://user-images.githubusercontent.com/51331982/185768360-4cd69097-183f-45e4-8873-0d29fabe626a.png)

### 26. Search in Rotated Sorted Array - Leetcode 33
  - First solution: O(n) trivial since we need to match every number in list with target and return the index
  - Second solution: Need O(logn) solution which would include a special type of binary search for rotated lists

### 27. Reorder List - Leetcode 143
  - L0 -> Ln -> L1 -> Ln-1 ...
  - First Solution:
    - Two pointer approach perhaps? two heads. First make pairs like L0 -> Ln , L1 -> Ln-1, ...
    - And then joining all of them. If for the last one, there is no pair, then it will be just a single number/node
    - Let's try this first
    
### 28. Binary Tree Level Order Traversal - Leetcode 102
  - Use queue
  - while queue is empty: level array for each level nodes, run a for loop inside while towards length of queue, and then popleft -> append left and right sibling in level
  - append whole level in result outside for
  - Time: O(n) | Space: O(n) for the queue length (n/2 at any stage max)

### 29. Validate BST - Leetcode 98
  - Recursion

### 30. Number of Islands - Leetcode 200
  - Long time no see
  - DFS or BFS anything will do to calculate number of connected components
  - Keep track of all visited squares in a separate visited matrix with all false initially
  - Start traversal from any node if that node is land ("1"), and it is not already visited
  - In the DFS_Util function, recurse for all four directions, check if the square indices are valid, and check visited status, and check if land or not, then recurse in all four directions (x+1, y) which is right, (x-1,y) left, (x,y+1) down, and (x, y-1) up. 
  - TC: O(mn) | SC: O(mn). SC can be reduced if we keep a visited set instead of a matrix. Keep track of only the visited squares which are ones.

### 31. Clone Graph - Leetcode 133
  - Deep Copy using DFS or BFS, anything will do
  - We have used DFS here
  - Need a hashmap to store all the nodes mapped from old to new (the deep copied ones)
  - Check node in oldToNew hashmap, if there, return oldToNew[node]
  - do Deepcopy = Node(node.val)
  - And link in hashmap with OldToNew[node] = deepcopy
  - Then do DFS inside the aux function
  - TC: O(V+E) | SC: O(V+E) since we made a deep copy

### 32. Pacific Atlantic Water Flow - Leetcode 417
  - Cells that can flow towards both atlantic and pacific ocean
  - The question isn't well explained in leetcode. Make sure you revise properly with the given example. It is almost similar to the DFS traversal done in 30th (LC 133) in that we have to traverse in all four directions, and check for validity of the cell
  - Calling the DFS_Util function with args row, column, visited, previousHeight, 4 times - twice for top and bottom, twice for left and right, since we have two oceans
  - Iterate a row-wise for loop through columns of heights, call DFS_Util twice, to fill up both atlanticSet and pacificSet so that we get cells that flow to those oceans from top and bottom
  - Iterate a col-wise for loop, call DFS_Util twice, so that we get cells that can flow towards ATL and PAC oceans from left and right now. 
  - Take the intersection of the two sets because we need cells that can have water that flows to both the oceans, and not just one.
  - TC: O(mn) | SC: O(mn) due to pac and atlSet, TC is O(mn) due to visited set checks, so that it doesn't go deep in recursive stack

### 33. Course Schedule - Leetcode 207
  - Detecting a cycle in a graph problem.
  - Convert the list into a defaultdict first
  - Use visited array length of numCourses, and currentPath array in order to store the visited nodes in the current DFS path
  - Loop through the nodes from 0 to numCourses-1 and perform if not visited[currentNode]: if not DFS_Util(visited, graph, currentPath, currentNode)
  - In DFS_Util, add in currentPath and make visited[currentNode] true, then loop through the neighbors and recurse.
  - Returning false and true can be problematic, so need to keep practising such questions for cycle detection
  - TC: O(V+E) | SC: O(V+E)

### 34. Number of Connected Components - Leetcode 323
  - Premium leetcode
  - Find number of CC, can be done using simple DFS. Count how many DFS processes are there, after every recursion backtracking is complete, increment the count of components
  - Next solution is via Union and Find. Do revise it again.
  - VVVV Important
  - ![Graph Theory](https://user-images.githubusercontent.com/51331982/208521114-c81d073d-22dd-41b9-ab2e-fe566b970d4e.png)
TC: O(V+E) SC: O(V+E) due to the rank and parent array taken in Union and Find, also the visted array taken in first approach
  
### 35. Graph Valid Tree - Lintcode 178
  - Premium
  - Indirectly we must calculate how to find a cycle in an undirected graph
  - Follow this program to revise the above concept.
  - Make adjacency list from the edges list given. Then create DFS_util(current, prev) inside main function so that we dont need to pass visited set in the function
  - loop through currentNode's neighbors. If any neighbor === prev, we have a backedge that we need to ignore, else it gives us a false positive on detection of a cycle, so continue with next itr
  - In false case, if not DFS_util(neigh, cur), return False, and at the end of func, return True
  - If null graph, return True
  - TC: O(v+e) SC: O(v+e)

### 36. Alien Dictionary - Leetcode Prem 269
  - A topological sort problem
  - Make the graph from one character to another. For e.g.: S = wert, T = wertff, so whenever we get the first differing letter after comparing a pair of strings word[i] and word[i+1] till its prefix (here, it is "wert"), the first letter thats different: t and f giving the connection t ---> f
  - t comes before f here, so make the connection in that way.
  - Similarly make the connection for each pair like this, giving way to number of graphs (could be connected or not).
  - If the input is invalid, such as in the words array, "abcd" comes before "abc", return "", also if there is a cycle in any graph, return null "" since we cannot order the letters such that any solution is possible. For e.g.: words = ["wee","abb", "waa"] , here w comes before a in the alien lang, but also a comes before w if we look at the last two words. This is invalid. So return ""
  - Step 1: Make the adjacency list for each character as a key in a defaultdict
  - Step 2: Create the graph, 
      i. considering the null case if prefix_s == prefix_t and len(s) > len(t), then return "".
      ii. Once we handle the above case, run a for loop inside tha main one, find the first differing character in S and T (if S[j] != T[j]) inside for j in range(min(len(s),len(t)))
      iii. fill the adjacency list and break
  - Step 3: Topological sort using DFS. DFS_UTIL returns True or False (found/not found cycle)
        - If cycle found, after DFS_Util func, run another loop for every character in adjacencylist, and if DFS_util(char), then return "", since we have an invalid input
  - Step 4: Reverse the finishtTimes stack and convert list into a string by "".join(finishTimes)
  
