# Time:
## Encoding takes O(n) time
## Decoding takes time depending on the length of the list and the number of digits in each string length
### Say length of strs is 200, and each string inside strs is 200 characters long
### Hence, inner while loop continues for 3 times per char (3 digits for 200), and subsequently, 200 times for the outer loop
## So, decoding will take O(200*3)
## Total is O(n + number_of_digits_in_each_char_length*n) ~ O(n) if number of digits is not that big
def encode(strs):
    # input: strs is a list of strings
    out = ""
    for s in strs:
        #append the length and a delimiter
        out += str(len(s)) + "#" + s
    return out

def decode(string):
    # input: str string after encoding
    output = []
    i = 0
    j = i
    while i < len(string):
        while string[j] != "#":
            j += 1
        l = int(string[i:j])
        output.append(string[j+1:j+1+l])
        i = j + 1 + l  # point to next length
        j = i # j points to i for start of next string info
    return output

if __name__ == "__main__":
    strs = ["lint","code","love","you"]
    print("Encoded string: ", encode(strs))
    print("Decoded string: ", decode(encode(strs)))