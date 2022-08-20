def lengthOfLongestSubstring(s):
    # Brute force is O(n^2) with checking every single substring and check for duplicates
    # could be O(n^3)
    # a b c a b c b b
    hashSet = set()
    left = 0
    right = 0
    maxLength = 0
    # keep expanding from 0
    for right in range(len(s)):
        while s[right] in hashSet:
            # if in hashset, keep sliding left ptr till we take care of all repeating chars
            hashSet.remove(s[left])
            left += 1
        hashSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    return maxLength

if __name__ == "__main__":
    s = "abcabcbb"
    print("Length of longest substring without repeating characters: ", lengthOfLongestSubstring(s))
