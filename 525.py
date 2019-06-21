class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        dic={}
        dic[0]=-1

        maxi=0

        for n in range(len(nums)):
            if nums[n]==0:
                sum-=1
            else:
                sum+=1

            if sum not in dic:
                dic[sum]=n
            else:
                maxi=max(maxi,n-dic[sum]) 
        return maxi