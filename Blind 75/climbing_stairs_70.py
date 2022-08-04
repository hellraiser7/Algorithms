# DP now
def climbStairsDP(n):
    # Calculate the recursion relation first
    # Do it for 2 steps, 3 steps, then 4. There will be a pattern emerging
    # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
    if (n <= 3):
        return n
    T = [0]*(n+1)
    
    T[2] = 2
    T[3] = 3

    #bottom-up
    for i in range(4,n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

def climbingStairsUtil(n):
    #base
    if (n <= 3):
        return n
    return climbingStairsUtil(n-1) + climbingStairsUtil(n-2)
    
if __name__ == "__main__":
    n = 6
    print(climbStairsDP(n))

