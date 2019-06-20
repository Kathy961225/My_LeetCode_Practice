class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        
        if n <=1:
            return n
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        dp[0][0] =1
        
        for i in range(1,n+1):
            
            for j in range(i,0,-1):
                if i == j:
                    dp[i][j] = 1
                    
                elif s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j+1] +2
                
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i-1][j])
                    
        return dp[n][1]