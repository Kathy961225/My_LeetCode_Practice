Longest uncommon should be a unique string and not a substring of other strings. Note that a unique string can be a substring of longer strings only.

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        def isSub(w1, w2, count):
            for i in w2:
                if i == w1[count]:
					count += 1
                if count == len(w1): 
					return True 
            return count == len(w2)
        
        
        d = collections.Counter(strs)
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            if d[strs[i]] == 1:
                res = any(isSub(strs[i], strs[j], 0) for j in range(i))        
                if res == False: return len(strs[i])
        return -1