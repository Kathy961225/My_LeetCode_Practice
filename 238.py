class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Forward: [1, 1*1, 1*1*2, 1*1*2*3] -> [1, 1, 2, 6]
        # Backward: [1*2*3*4, 1*4*3, 2*4, 6*1] -> [24, 12, 8, 6]
        
        out = [0] * len(nums)
		
		# Forward pass
        p = 1
        for i in range(len(nums)):
            out[i] = p
            p *= nums[i]
            
		# Backward pass
        p = 1
        for i in reversed(range(len(nums))):
            out[i] *= p
            p *= nums[i]
            
        return out

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return None
        
        res = len(nums) * [1]
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
            
        back = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * back
            back *= nums[i]
            
        return res