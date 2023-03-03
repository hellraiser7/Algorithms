class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            # from end of string, bottom up approach, towards the beginning
            for word in wordDict:
                # check for length of current character window, from i to i+len(w)
                # i + len(w) needs to be lesser than len(s) in order to be inside the bounds 
                # when we are slicing it to check for the presence of the word in wordDict
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    # cache it
                    dp[i] = dp[i+len(word)]
                    # nee tc ode
                if dp[i]:
                    break
        return dp[0]
