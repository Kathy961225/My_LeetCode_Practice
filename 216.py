class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtracking(0,[],k,n)
        return self.res
        
        
    def backtracking(self, start, cur, k, n):
        if len(cur) == k and sum(cur) == n:
            self.res.append([i for i in cur])
        if start > k or sum(cur) > n:
            return
        
        if cur==[]:
            for i in range(1,10):
                cur=[i]
                self.backtracking(1,cur,k,n)
                cur.pop()
        else:
            for i in range(cur[-1]+1, 10):
                cur.append(i)
                self.backtracking(start+1,cur,k,n)
                cur.pop()