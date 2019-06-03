class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        
        if len(B)%len(A) == 0:
            t = len(B)/len(A)
        else:
            t = len(B)/len(A) + 1
        
        for i in range(0,2):
            if B in A*(t+i):
                return t+i
            
        return -1