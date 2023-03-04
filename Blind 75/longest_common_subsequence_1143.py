class Solution:
    def longestCommonSubsequence_recursion(self, text1: str, text2: str) -> int:
        # recursion
        dp = {}
        def LCS(i,j):
            if (i,j) in dp:
                return dp[i,j]
            if i < 0 or j < 0:
                # index lesser than 0 means there is an empty string, so return 0
                return 0
            if text1[i] == text2[j]:
                # equality, we extend our answer
                dp[i,j] = 1 + LCS(i-1,j-1)
            # else we take maximum of removing one letter from each
            else:
                dp[i,j] = max(LCS(i,j-1), LCS(i-1,j))
            return dp[i,j]

        return LCS(len(text1)-1,len(text2)-1)
