Step 1: check array length, needs to be greater than 1
Step 2: if k == 0, return true if two consecutive items are 0
Step 3: Use presum and dictionary to record already appeard sums(%k). If the newly added sum (%k) is in the dic, it tells the newly added slice of array meets the criteria.
For example, if presum = 3, k =5, we have presume%k = 3 (add to dictionary), so if you added two more numbers 4, and 1, the presume will becomes 8, 8 %5 = 3, and 3 is already in dictionary, so we know the newly added two numbers must be divsible by k(5)
Step 4: care for the two corner cases:
a: what if the newly added value is the same as k: for example (1,3,5) k = 5, so we need to exclude this situation: nums[i] != k
b: what if the first two values are the same as k: for example (1,1), k=1, so we can include this situation by adding nums[0] == nums[1] == k
Either a or b can happen, so we use or in between

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cur_sum = 0
        cache = {0:-1}
        
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if k!=0:
                cur_sum %= k
            if cur_sum in cache:
                if i - cache[cur_sum] > 1:
                    return True
            else:
                cache[cur_sum] = i
        return False