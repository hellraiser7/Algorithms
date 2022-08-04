def hammingWeight(n):
    sum = 0
    while n:
        # do modulo with 2, we get 1 if it is set (odd number)
        # then shift right for the next bit comparison
        sum += n % 2
        n = n >> 1
    return sum

def hammingWeightGenius(n):
    # genius approach, no need to know this by heart
    # if you remember, you remember
    # it goes on for a lot lesser than O(32)
    sum = 0
    while n:
        n = n & (n-1)
        sum += 1
    return sum

if __name__ == "__main__":
    n = (2147483649) # 10000000000000000000000000000001
    print(hammingWeight(n))

        