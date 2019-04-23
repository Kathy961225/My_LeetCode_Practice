We will start off by doing an O(n) dp solution, where dp[i] denotes the number of ways of decoding the sequence starting at the index i.
O(n) time, O(n) space.

from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(lambda:0)
        dp[len(s)] = 1
        dp[len(s)-1] = 1 if s[len(s)-1] != "0" else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == "0": #A sequence starting with zero will never be valid
                dp[i] = 0
                continue
            if int(s[i: i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]

单个字母为一条路的时候dp[i+1]，两个字母为一条路的时候dp[i+2]

Now let's try to better the space complexity to O(1). We take advantage of the fact that we only ever need the previous two values of the dp, and going forward for dp[i+1], the most we will need is dp[i] and dp[i-1].
Hence, we can just replace the dp matrix with two variables a and b:
class Solution:
    def numDecodings(self, s: str) -> int:
        a = 1
        b = 1 if s[len(s)-1] != "0" else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == "0": #A sequence starting with zero will never be valid
                a = 0
                a, b = b, a
                continue
            if int(s[i: i+2]) <= 26:
                a = b + a
            else:
                a = b
            a, b = b, a
        return b
