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

