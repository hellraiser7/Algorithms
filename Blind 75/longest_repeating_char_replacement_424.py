from collections import defaultdict
def characterReplacement(s, k):
    # Sliding window with hashmap gives O(26.n) TC and O(26) SC
    # left and right pointers
    # Check the number of other characters that can be replaced by doing lenOfSubStr - maxCount <= k
    # if true, then we can replace all the other characters and result = length of current window/substr
    # if not, then slide left pointer and take care of new window in next itr
    # also remove the frequency of that char where left was sitting, before sliding
    result = 0
    left = 0
    right = 0
    hashmap = defaultdict(int)
    # get the hashmap first
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabets:
        hashmap[letter] = 0
    # logic
    for right in range(len(s)):
        hashmap[s[right]] += 1
        currentWindowLength = right - left + 1
        if currentWindowLength - max(hashmap.values()) <= k:
            result = currentWindowLength
        else:
            # remove from hashmap and shift left pointer
            hashmap[s[left]] -= 1
            left += 1
    return result

if __name__ == "__main__":
    s = "AABABBA"
    k = 2
    print("Longest Substring length with repeating characters: ", characterReplacement(s, k))