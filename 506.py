class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortednums = sorted(nums, reverse=True)
        l = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        l = {x: l[i] if i < 3 else str(i + 1) for i, x in enumerate(sortednums)}
        return [l[x] for x in nums]