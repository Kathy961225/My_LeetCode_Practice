class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        rows=len(board)
        cols=len(board[0])

        queue=[]
        visited=set()
        for i in range(rows):
            for j in range(cols):
                if (i==0 or i==rows-1 or j==0 or j==cols-1) and board[i][j]=='O':
                    queue.append((i,j))
                    visited.add((i,j))
        
        while queue:
            i,j = queue.pop(0)
    
            x_change=[1,-1,0,0]
            y_change=[0,0,1,-1]
            for ind in range(4):
                x=x_change[ind]+i
                y=y_change[ind]+j
                if x<0 or y<0 or x>=rows or y>=cols or (x,y) in visited or board[x][y]=='X':
                    continue
                queue.append((x,y))
                visited.add((x,y))
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and not (i,j) in visited:
                    board[i][j]='X'