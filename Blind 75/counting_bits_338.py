def countBits(n):
    # can use the previous program function: number of set bits count
    # but also can have a single pass
    arr = []
    for i in range(n+1):
        arr.append(getSetBits(i))
    return arr

def countBitsOnePass(n):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = dp[i>>1] + (i%2)
    return dp

def getSetBits(n):
    sum = 0
    while n:
        n = n & (n-1)
        sum += 1
    return sum

if __name__ == "__main__":
    n = 5
    print("count bits with brute force: ", countBits(n))
    print("count bits with optimized solution: ", countBitsOnePass(n))