class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        directMap = self.getDirectConnect(M)
        visited = set()
        res = 0
        for i in range(len(M)):
            if i not in visited:
                res += 1
                self.dfs(directMap, i, visited)
                
        return res         
                
         
    def getDirectConnect(self, M):
        adjMap = collections.defaultdict(set)
        
        for j in range(len(M[0])):
            for i in range(len(M)):
                if M[i][j] == 1:
                    adjMap[i].add(j)
        
        return adjMap
    
    def dfs(self, adjMap, idx, visited):
        
        visited.add(idx)
        
        for nei in adjMap[idx]:
            if nei not in visited:
                self.dfs(adjMap, nei, visited)