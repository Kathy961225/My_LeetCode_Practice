class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2: return False

        for i in range(1, n//2 + 1):
            if n%i == 0 and s[:i] * (n//i) == s:
                return True

        return False