class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(i , coins , amount,dp):
            if amount < 0 : 
                return float('inf') #as this path is not possbile further
            if amount  == 0 :
                return 0
            if i==len(coins):#all coins seen yet no answer
                return float('inf')
            if dp[i][amount]!=-1:
                return dp[i][amount]
            # pick 
            pick = 1+  solve(i , coins , amount - coins[i],dp)
            # not pick
            notPick =  solve(i + 1 , coins , amount,dp)
            dp[i][amount] = min(pick,notPick)
            return  dp[i][amount]
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)]
            for _ in range(len(coins)+1)]

        ans = solve(0 , coins , amount , dp)
        if ans == float('inf'):
            return -1
        return ans