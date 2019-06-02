https://leetcode.com/problems/maximal-rectangle/discuss/277448/Python-Height-x-Width

def maximalRectangle(matrix):
	sz, n = 0, len(matrix) and len(matrix[0])
	h = [0] * (n+1)
	for row in matrix:
		for i in range(n):
			h[i] = h[i] + 1 if row[i] == '1' else 0
		w = [-1]
		for j in range(n+1):
			while h[j] < h[w[-1]]:
				height = h[w.pop()]
				sz = max(sz, height * (j-1-w[-1]))
			w.append(j)
	return sz