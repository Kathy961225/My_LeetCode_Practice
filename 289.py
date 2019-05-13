class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return
        
        row = len(board)
        col = len(board[0])
        

        
        for i in range(0, row):
            for j in range(0, col):
                self.helper(board,i,j,row,col)
        
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == -2:
                    board[i][j] = 1
        
        
    
    
    
    
    def helper(self, board, i, j, row, col):        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        count = 0

        for (x,y) in directions:
            if 0<=i+x<row and 0<=j+y<col and abs(board[i+x][j+y])==1:
                count += 1
                    
        if count < 2 or count > 3:
            if board[i][j] == 1:
                board[i][j] = -1
        elif count == 3:
            if board[i][j] == 0:
                board[i][j] = -2
        