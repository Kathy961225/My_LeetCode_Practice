class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        import collections
        
        res = collections.Counter(nums)
        
        for item in res:
            if res[item] != 3:
                return item