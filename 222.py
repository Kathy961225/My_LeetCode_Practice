class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return nums
            else:
                return [nums[0]]
        ans = []
        nums.sort()
        pre = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != pre:
                count = 1
            
            if nums[i] == pre:
                count += 1
            if count > len(nums)/3 and nums[i] not in ans:
                ans.append(nums[i])
            pre = nums[i]
        
        return ans