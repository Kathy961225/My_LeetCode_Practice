 def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(word, board, i, j):
                    return True
        return False
    
    def helper(self, word, board, x, y):
        if board[x][y] != word[0] or board[x][y] == '#':
            return False
        
        if len(word) == 1: return True
            
        c = board[x][y]
        board[x][y] = '#'
        # down, right, up, left to search
        for dx, dy in zip([1, 0, -1, 0],[0, 1, 0, -1]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if self.helper(word[1:], board, nx, ny):
                    return True
        board[x][y] = c
        return False