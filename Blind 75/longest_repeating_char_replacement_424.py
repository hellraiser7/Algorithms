from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # make the hashmap count pairing
        for letter in alphabets:
            hashmap[letter] = 0
        result = 0
        left = 0
        right = 0
        for right in range(len(s)):
            # add in freq set
            hashmap[s[right]] += 1
            currentWindowLength = right - left + 1
            if currentWindowLength - max(hashmap.values()) <= k:
                # other characters that need to be replaced must satisfy this condition
                result = currentWindowLength
            else:
                # shift the left pointer and also remove that count from hashmap
                hashmap[s[left]] -= 1
                left += 1
        return result
