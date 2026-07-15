class Solution:
    def longestPalindrome(self, s: str) -> str:
        # pal check function using 2tptr return bool
        # def isPalindrome(s, l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        # this was iterative now recurse
        # def isPal(i,j,string):
        #
        #     if i>=j:#means overllaping hogye mtlb sahi the pichle srteps
        #         return True
        #     if string[i] == string[j]:#correct contirnue
        #         return isPal(i+1,j-1,string)
        #     else:
        #         return False
        # above was top donw
        # now top down dp tab
        def isPal(i, j):
            if i >= j:  # base case overlapping one
                return True
            if dp[i][j] != -1:  # alrady seen
                return dp[i][j]
            if s[i] == s[j]:  # checks if same then move fwd
                dp[i][j] = isPal(i + 1, j - 1)
            else:  # noteqauol return false
                dp[i][j] = False
            return dp[i][j]

        ans = s[0]
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        # Generate all substrings
        for start in range(n):
            for end in range(start, n):
                # Check if current substring is palindrome
                if isPal(start, end):
                    # Update answer if current palindrome is longer
                    currStrLen = end - start + 1
                    if currStrLen > len(ans):
                        ans = s[start : end + 1]
        return ans
