class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        dp = [0]*len(nums)
        
        dp[0] = 1

        
        for i in range(1, len(nums)):
            cur = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    cur = max(cur, dp[j])
            dp[i] = cur + 1

            
        return max(dp)