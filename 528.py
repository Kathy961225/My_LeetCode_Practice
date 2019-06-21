class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.sum = sum(w)
        self.len = len(w)
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.cum_sum = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        r = random.randint(1, self.sum)
        
        low, high = 0, self.len - 1
        while low < high:
            mid = low + (high - low)//2
            if r > self.cum_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low