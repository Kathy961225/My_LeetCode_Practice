class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        if not matrix:
            return
        
        res = []
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                res.append(matrix[row][col])
                
        res.sort()
        
        return res[k-1]