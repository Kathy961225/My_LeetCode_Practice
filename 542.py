class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # trivial case
        n = len(matrix)
        if n < 1:
            return matrix
        m = len(matrix[0])
        if m < 1:
            return matrix
        
        q = collections.deque()
        
        # enqueue all zeros in a bfs layer/breadth and move outwards
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = -1
        while q:
            u = q.popleft()
            urow = u[0]
            ucol = u[1]
            for adj in [(0,1),(1,0),(0,-1),(-1,0)]:
                v = (urow + adj[0],ucol + adj[1])
                vrow = v[0]
                vcol = v[1]
                
                # out of bound check
                if vrow < 0 or vrow >= n:
                    continue
                if vcol < 0 or vcol >= m:
                    continue
                    
                # skip visited
                if matrix[vrow][vcol] >= 0:
                    continue
                    
                # update distance
                matrix[vrow][vcol] = matrix[urow][ucol] + 1
                
                q.append(v)
        return matrix