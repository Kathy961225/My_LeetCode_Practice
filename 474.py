class Solution(object):
	def findMaxForm(self, strs, m, n):
		self.memoi = {}
		return self.helper(0, strs, m, n)

	def helper(self, index, strs, m, n):
		#cache result with a dictionary
		if (index, m, n) in self.memoi:
			return self.memoi[index, m, n]
			
		#base case
		if index == len(strs) - 1:
			self.memoi[index, m, n] = 1 if strs[index].count("0") <= m and strs[index].count("1") <= n else 0
			return self.memoi[index, m, n]

		#if we dont choose this string
		res = self.helper(index + 1, strs, m, n)
		
		#if m and n are enough to choose this string, get the max between the result of choosing and not choosing
		if m >= strs[index].count("0") and n >= strs[index].count("1"):
			res = max(res, 1 + self.helper(index + 1, strs, m - strs[index].count("0"), n - strs[index].count("1")))

		self.memoi[index, m, n] = res
		return res