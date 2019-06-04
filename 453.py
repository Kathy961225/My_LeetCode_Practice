The greedy heuristics here is that we always add |max-min| to all elements except the maximum until all elements are equal. In such way, we keep making current minimum catch up with maximum without wasting any unnecessary steps.
Suppose we now sort our array as {X1,...,Xn}. For first catch up, we take (Xn - X1) steps. And now Xn-1 becomes the new maximum as Xn + Xn-1 - X1 and new minimum is Xn. So next catch take (Xn-1 - X1) steps. And similiarly, for ith iteration, the catch up takes (Xi - X1) steps. So total number of step would be ∑Xi - X1 * n or sum(X) - min(X) * len(X).

def minMoves(nums):
	return sum(nums) - min(nums)*len(nums)

https://leetcode.com/problems/minimum-moves-to-equal-array-elements/discuss/299009/Java-easy-with-detailed-explanation...
