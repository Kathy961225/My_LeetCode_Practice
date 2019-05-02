class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not grid:
            return 
        
        oldcolor = grid[r0][c0]
        
        not_color = []
        
        self.dfs(grid, r0, c0, oldcolor)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '#':
                    if i>0 and j>0 and i<len(grid)-1 and j<len(grid[0])-1 and grid[i+1][j] == '#' and grid[i-1][j] == '#' and grid[i][j+1] =='#' and grid[i][j-1] == '#':
                        not_color.append([i,j])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '#':
                    if [i,j] not in not_color:
                        grid[i][j] = color
                    else:
                        grid[i][j] = oldcolor
        return grid
            
        
        
    def dfs (self, grid, i, j, oldcolor):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != oldcolor:
            return
        
        grid[i][j] = '#'
        
        self.dfs(grid, i+1, j, oldcolor)
        self.dfs(grid, i-1, j, oldcolor)
        self.dfs(grid, i, j+1, oldcolor)
        self.dfs(grid, i, j-1, oldcolor)
        
        
            