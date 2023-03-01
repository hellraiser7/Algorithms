class Solution:
    def countSubstrings(self, s: str) -> int:
        # O(n^3) is brute force, checking every single substring
        # check from each center character, expand outwards
        # That gives O(n^2)
        count = 0
        def countPalindromes(s,left,right):
            count = 0
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                count += 1
                # modify left and right
                left -= 1
                right += 1
            return count
        for i in range(len(s)):
            # odd length palindromes, we have left and right pointers as the same
            count += countPalindromes(s,i,i)
            # even length counting
            # now left and right are adjacent characters
            count += countPalindromes(s,i,i+1)

        return count
    

if __name__ == "__main__":
    S = Solution()
    print(S.countSubstrings("abcd"))
