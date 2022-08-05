import re


def reverseBits(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    str = "";
    if (len(binary) < 32):
        str = "0"*(32-len(binary))
    final_binary = int(reversed_binary + str, 2)
    return final_binary

def reverseBitsLoop(n):
    # % 2 and then right shift to another string
    bstr = ""
    while n:
        bstr += str(n % 2)
        n >>= 1
    if (len(bstr) < 32):
        bstr += "0"*(32 - len(bstr)) # to accomodate the trailing zeros
    return int(bstr, 2)

if __name__ == "__main__":
    print(reverseBits(int("00000010100101000001111010011100",2)) == 964176192)
    print(reverseBitsLoop(int("00000010100101000001111010011100",2)) == 964176192)
    # validating the example test case, should come as True