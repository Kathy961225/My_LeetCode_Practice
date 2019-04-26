# O(1) space    
def maxProduct2(self, nums):
    if not nums:
        return 
    locMin = locMax = gloMax = nums[0]
    for i in xrange(1, len(nums)):
        if nums[i] < 0:
            tmp = locMax
            locMax = max(locMin*nums[i], nums[i])
            locMin = min(tmp*nums[i], nums[i])
        else:
            locMax = max(locMax*nums[i], nums[i])
            locMin = min(locMin*nums[i], nums[i])
        gloMax = max(gloMax, locMax)
    return gloMax
 
# O(1) space    
def maxProduct(self, nums):
    if not nums:
        return 
    locMin = locMax = gloMax = nums[0]
    for i in xrange(1, len(nums)):
        tmp = locMin
        locMin = min(locMin*nums[i], nums[i], locMax*nums[i])
        locMax = max(tmp*nums[i], nums[i], locMax*nums[i])
        gloMax = max(gloMax, locMax)
    return gloMax