class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return
        
        
        res = []
        
        end = '#'
        start = nums[0]
        for i in range(1, len(nums)+1):
            if i < len(nums) and nums[i] == nums[i-1]+1 :
                end = nums[i]
            else:
                if end != '#':
                    s = str(start) + "->" + str(end)
                else:
                    s = str(start)
                
                res.append(s)
                if i < len(nums):
                    start =nums[i]
                    end = "#"
                
        
        return res