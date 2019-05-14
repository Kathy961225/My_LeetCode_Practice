class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s and not t:
            return True
        
        if not s:
            return True
        
        s = list(s)
        
        for i in t:
            if not s:
                return True
            if i == s[0]:
                s.remove(s[0])
                
        return not s