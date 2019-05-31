class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        bsx = []    # bxs[]:b->buy, s->sell, x->cooldown
        for i in range(len(prices)):
            if i==0:
                bsx = [-prices[i], 0, 0]
                continue
                
            bsx = [
                max(bsx[-1] - prices[i], bsx[0]),
                bsx[0] + prices[i],
                max(bsx)
            ]
        return max(bsx)