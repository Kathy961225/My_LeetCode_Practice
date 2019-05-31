class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        sum_ = sum(nums)
        
        if sum_ % 2 == 1:
            return False
        
        target = sum_/2
        
        dp = [False] * (target+1)
        
        dp[0] = True
        
        for num in nums:
            for i in range(target, -1, -1):
                if dp[i]:
                    if (num + i) <= target:
                        dp[num + i] = True
                if dp[target]:
                    return True
                
        return False