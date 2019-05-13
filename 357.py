class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        if n == 0:
            return 1
        
        dp = [0] *(n+1)
        dp[0] = 1
        dp[1] = 10
        
        for i in range(2, n+1):
            val = 9
            for j in range(0, i-1):
                val *= (9-j)
            dp[i] = dp[i-1] + val
            
        return dp[-1]