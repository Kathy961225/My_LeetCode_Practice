class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return 0
        
        import collections
        
        count_map = collections.Counter(nums)
        
        res = []
        count = 0
        for item in count_map:
            if count_map[item] != 2:
                res.append(item)
                count += 1
            if count == 2:
                return res
            
        return res