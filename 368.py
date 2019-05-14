class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        result = [[i] for i in nums]
        for j in range(1, len(nums)):
            for i in reversed(range(0, j)):
                if nums[j]%nums[i] == 0 and len(result[i]) >= len(result[j]):
                        result[j] = result[i]+ [nums[j]]

        return max(result, key=len) if len(result) != 0 else []