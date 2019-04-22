class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        if nums == []:
            return None
        
        res = {}
        
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        
        for n in res:
            if res[n] == 1:
                return n