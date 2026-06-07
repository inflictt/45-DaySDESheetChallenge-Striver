class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # now the dp memo
        def solve(i , j , dp) :
            if i == m-1 and j ==n-1 : 
                return 1
            # check out of bounds
            if i<0 or j<0 or i>=m or j>=n:#as out of limit/index
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            right = solve(i,j+1,dp)#cols + 1 happens
            bottom = solve(i+1,j,dp)#rows + 1 happens
            dp[i][j] = right+bottom 
            return dp[i][j]
        dp = [[-1 for i in range(n+1)]for j in range(m+1)]
        ans = solve(0, 0 , dp )
        return ans
    

    # Recursive + memoization
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # basic recurision approach - top down done
        def solve(i , j) :
            if i == m-1 and j ==n-1 : 
                return 1#as req path was this only so ret1
            # check out of bounds
            if i<0 or j<0 or i>=m or j>=n:
                return 0 #as out of limit/index
            # else we are good to go 
            right = solve(i,j+1)#cols + 1 happens
            bottom = solve(i+1,j)#rows + 1 happens
            return right+bottom 
        ans = solve(0, 0 )
        return ans