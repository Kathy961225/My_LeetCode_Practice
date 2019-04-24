DP解法的两大难点，定义dp数组跟找出状态转移方程，先来看dp数组的定义，这里我们就用一个一维的dp数组，
其中dp[i]表示范围[0, i)内的子串是否可以拆分，注意这里dp数组的长度比s串的长度大1，是因为我们要handle空串的情况，
我们初始化dp[0]为true，然后开始遍历。注意这里我们需要两个for循环来遍历，因为此时已经没有递归函数了，所以我们必须要遍历所有的子串，
我们用j把[0, i)范围内的子串分为了两部分，[0, j) 和 [j, i)，其中范围 [0, j) 就是dp[j]，范围 [j, i) 就是s.substr(j, i-j)，
其中dp[j]是之前的状态，我们已经算出来了，可以直接取，只需要在字典中查找s.substr(j, i-j)是否存在了，
如果二者均为true，将dp[i]赋为true，并且break掉，此时就不需要再用j去分[0, i)范围了，
因为[0, i)范围已经可以拆分了。最终我们返回dp数组的最后一个值，就是整个数组是否可以拆分的布尔值了

https://www.cnblogs.com/grandyang/p/4257740.html


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(n):
            if f[i]:
                for j in dict:
                    l = len(j)
                    if i+l<=n and s[i:i+l] == j:
                        f[i+l] = True
        return f[n]


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        t = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if word == s[i-len(word):i] and t[i-len(word)]:
                    t[i] = True
                    break
        return t[-1]