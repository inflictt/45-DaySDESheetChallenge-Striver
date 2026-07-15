class Solution:
    def minInsertions(self, s: str) -> int:
        def solve(i, j, string, dp):
            if i >= j:  # ovlp condition
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:  # strings equal
                dp[i][j] = solve(i + 1, j - 1, string, dp)
                return dp[i][j]
            else:  # didnt match then has to 2. path to try either i or j
                dp[i][j] = 1 + min(
                    solve(i + 1, j, string, dp), solve(i, j - 1, string, dp)
                )
                return dp[i][j]

        if s == s[::-1]:
            return 0
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        i, j, string = 0, n - 1, s
        ans = solve(i, j, string, dp)
        return ans
