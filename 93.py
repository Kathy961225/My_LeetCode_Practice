If the length of current is 4 and start point equals to the length of s, then add it to the result.
Then check the next 3 number from index start, and make sure that it does not exceed the total length of s. If the first digit is 0 and i>start, like 09 or 01, then skip those conditions.

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def bt(start, current):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return
            for i in xrange(start+1, min(start+4, len(s)+1)):
                if i-1>start and s[start] == '0':
                    continue
                a = s[start:i]
                if 0 <= int(a) <= 255:
                    current.append(a)
                    bt(i, current)
                    current.pop()
        
        result = []
        bt(0, [])
        return result