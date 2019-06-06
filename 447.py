class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = [0] * 32
        for x in nums:
            b = bin(x)[2:][::-1]
            for i, v in enumerate(b):
                count[i] += int(v)
        
        # return sum([(N-c)*c for c in count])
        ans = 0
        N = len(nums)
        for i in range(32):
            ans += (N - count[i]) * count[i]
        return ans