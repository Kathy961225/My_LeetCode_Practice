https://leetcode.com/problems/gas-station/discuss/253354/python-O(n)-3-alternative-solutioins-with-rough-proofs

class Solution:
    def canCompleteCircuit(self, gas: 'List[int]', cost: 'List[int]') -> 'int':
        i, n = 0, len(gas)
        while i < n:
            s = 0
            for j in range(i, i+n):
                s += gas[j%n] - cost[j%n]
                if s < 0: break
            if s >= 0: return i
            i = j+1         # because for any i<k<=j, sum[k,j] == sum[i,j]-sum[i,k-1] <= sum[i,j] < 0
        return -1


https://leetcode.com/problems/gas-station/discuss/239761/Python-20ms-simplest-explanation

We compute the difference between amount of gas and the cost to get to the next station, at each station. This is the net gas reward at each station. Clearly to make a full circuit, the total net gas reward needs to be greater than or equal to 0. If it isn't return -1.

Finally, we want to find s[i:j] such that the cumulative sum of s[i:j] is maximized and return i. Intuitively, this is because we want to 'build up' the gas reward for when we cross the stations that have a negative net gas reward. To do this, simply track a cumulative sum and reset it when it goes below 0.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        differences = [gas[i] - cost[i] for i in range(0, len(gas))]
        if sum(differences) < 0:
            return -1
        currentSum = 0
        startIndex = 0
        for i, diff in enumerate(differences):
            currentSum += diff
            if currentSum < 0:
                currentSum = 0
                startIndex = i+1
        return startIndex