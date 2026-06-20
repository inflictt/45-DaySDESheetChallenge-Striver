class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(idx , string,dp):
            if len(string)==idx:
                return True
            if dp[idx]!=-1:
                return dp[idx]
           
            # else make and check
            for i in range(idx,len(string)):
                temp =  string[idx:i+1]
                if temp in wordDict and solve(i+1,string,dp):
                    dp[idx] = True
                    return True
            dp[idx] = False
            return dp[idx]
        idx , string =0 , s
        dp = [-1 for _ in range(len(s)+1)]        
        return solve(idx , string,dp)