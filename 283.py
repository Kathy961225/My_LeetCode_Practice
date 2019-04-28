class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return None
        
        cur_index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[cur_index] = nums[i]
                cur_index += 1
        
        for i in range(cur_index, len(nums)):
            nums[i] = 0