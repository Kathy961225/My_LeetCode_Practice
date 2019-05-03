2 of a painpoints for most of DP problems:
1, what does dp[i,j] means
Here, we use dp[i,j] to to represent answer to maxUncrossedLines(self,A[:i],B[:j])
2, corner cases, index error. Some times, we have problem if i == 0 or j == 0, since it uses dp[-1,j] dp[i,-1], which would return index error.
Here, we will start working on i = 1 or j = 1 by using i = 0 or j = 0.
We use dp[i,j] to to represent answer to maxUncrossedLines(self,A[:i],B[:j])

class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        m = len(A)
        n = len(B)
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i,j] = dp[i-1, j-1] + 1
                else:
                    dp[i,j] = max(dp[i-1, j],dp[i,j-1])
        
        return dp[m, n]
