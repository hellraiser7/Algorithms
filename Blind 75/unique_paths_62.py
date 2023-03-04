class Solution:
    def uniquePaths(self, m, n):
        # Recursion with memoization: TC O(mn) SC O(mn)
        # caching mechanism automatically prevents recomputation of values
        # So prevents widening of the decision tree
        # base
        def dfs(i,j):
            # out of bounds
            if i >= m or j >= n:
                return 0
            # reached the end, return 1 way to reach
            if i == m-1 and j == n-1:
                return 1
            # recursive relation
            return dfs(i+1,j) + dfs(i,j+1)
        return dfs(0,0) # start index
    def uniquePathsDP(self, m, n):
        # Initialize all cells to 1, and start loop from (1,1)
        # since only one way to reach (0,0), (0,1) and (1,0) and values already 1
        dp = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                # does not matter we go column wise or row wise
                # two ways to reach cell i,j -> from up (i-1,j) and left (i,j-1)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

S = Solution()
print(S.uniquePathsDP(3,7))
            
