class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
        temp = [a,b,c]
        temp.sort()
        a = temp[0]
        b = temp[1]
        c = temp[2]
    
        
        distance1 = abs(a-b)
        distance2 = abs(b-c)
        
        
        if distance1 == 1 and distance2 == 1:
            return [0,0]
        else:
            if b - a == 2 or b - a == 1 or c - b == 2 or c - b == 1:
                minmove = 1
            else:
                minmove = 2
            return [minmove, max(c-a-1, max(distance1, distance2)-1)-1]