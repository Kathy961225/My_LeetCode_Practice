class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        A = [ord(c) - ord('a') for c in p]
        n = len(A)
        dp = [1] * n
        res = 0
        cnt = collections.Counter()
        for i in range(n):
            if i > 0 and A[i] == (A[i - 1] + 1) % 26:
                dp[i] = dp[i - 1] + 1
            cnt[A[i]] = max(cnt[A[i]], dp[i])
        return sum(cnt.values())