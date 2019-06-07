from collections import defaultdict
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hc = defaultdict(int)
        for ch in hand:
            hc[ch] += 1
        
        def find(board, hc):
            if not board:
                return 0
            
            N = len(board)
            i = 0
            while i < N:
                j = i+1
                while j < N+1:
                    if j < N and board[i] == board[j]:
                        j += 1
                        continue
                    if j - i >= 3:
                        return find(board[:i]+board[j:], hc)
                    i = j
                    break
            
            i = 0
            res = []
            while i < N:
                j = i+1
                while j < N+1:
                    if j < N and board[i] == board[j]:
                        j += 1
                        continue
                    
                    need = (3 - j + i)
                    if hc[board[i]] >= need:
                        hc[board[i]] -= need
                        r = find(board[:i]+board[j:], hc)
                        r = r + need if r != -1 else -1
                        res.append(r)
                        hc[board[i]] += need
                    i = j
                    break
            
            if res == [-1] * len(res):
                return -1
            
            return min([r for r in res if r != -1])
        
        return find(board, hc)