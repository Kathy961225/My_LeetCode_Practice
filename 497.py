class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.count = []
        self.tot = 0
        for x1, y1, x2, y2 in rects:
            result = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            self.count.append(result)
            self.tot += result
        self.tot -= 1

    def pick(self):
        """
        :rtype: List[int]
        """
        index = random.randint(0, self.tot)
    
        for i in range(len(self.count)):
            if index < self.count[i]:
                # Pick point at index
                x0 = min(self.rects[i][0], self.rects[i][2])
                xL = abs(self.rects[i][0] - self.rects[i][2]) + 1
                y0 = min(self.rects[i][1], self.rects[i][3])
                x = x0 + index % xL
                y = y0 + index / xL
                return [x, y]
                
            else:
                index -= self.count[i]