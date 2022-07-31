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
    - next is current->next
    - reversing logic aka current->next = previous
    - now shifting the pointers: previous = current, current = next
    - After first iteration, the llist becomes something like: 1 -> 2 -> 3 -> 4 -> x
                                                                    p    n,c
                                                                    
