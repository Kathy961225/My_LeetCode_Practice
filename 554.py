from collections import Counter
class Solution(object):
	def leastBricks(self, wall):
		cc = Counter()
		for line in wall:
			line_length = 0
			for index, brick_length in enumerate(line):
				if index == len(line) - 1:
					break
				line_length += brick_length  #可以切的位置
				cc[line_length] += 1
		return len(wall) - cc.most_common()[0][1] if cc.most_common() else len(wall)
		#总长度-最大可以切的位置  等于被切掉的位置