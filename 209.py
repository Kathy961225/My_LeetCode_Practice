class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import sys
        res = sys.maxint
        left = 0
        cur_sum = 0
        
        for i in range(0, len(nums)):
            cur_sum += nums[i]
            while cur_sum >= s:
                res = min(res, i-left+1)
                cur_sum -= nums[left]
                left += 1
                
                
        if res == sys.maxint:
            return 0
        else:
            return res