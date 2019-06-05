def validSquare(self, p1, p2, p3, p4):
    def dSquareSum(a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2 # doing sqrt is unnecessary
        
    sq_sums = {}
    for (a, b) in [(p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4)]:
        dss = dSquareSum(a, b)
        if dss in sq_sums: sq_sums[dss] += 1
        else: sq_sums[dss] = 1
                
    sqlen_edge, sqlen_diag = min(sq_sums.keys()), max(sq_sums.keys())
    return sq_sums[sqlen_edge] == 4 and sq_sums[sqlen_diag] == 2
	
	# check if right angle
	# return sq_sums[sqlen_edge] == 4 and sqlen_edge*2 == sqlen_diag