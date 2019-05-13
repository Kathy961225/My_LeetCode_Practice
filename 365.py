class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        
        # Explanation: 
        # Key idea is that z litres is measurable using jugs of size x and y only if , z is a linear combination of x and y.
        # Reasoning for key idea : 
        # basically only options we have to solve the issue is - either pour water of amount x or y (which is positive multiplication constant on x or y) or a choice of emptying x or y (which is negative multiplication constant on x or y). hence for z to be measurable by x and y, z has to be 
z = sx+ly (where s and l are integer constants, we dont need to know s and l to solve our problem :))
        # So, in positive case where, z = kx + ly where k and l are constants, z is measurable. 
        # Now, if g is gcd of x and y, then z = kag + lbg where a and b are constants 
        # So, z = (ka+lb)g -> which suggests z must be divisible by g in order for z to be measurable by x and y. 
        # AND 
        # x + y must be equal or greater than z, otherwise we can fill up x and y both, but still they will sum up less than z. Hence, z won't be measurable if x + y < z
        # using that logic, we can say answer is:
        # return true if z % gcd(x, y) == 0 and x + y >= z
        
        def gcd(x, y):
            #Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                remainder = x % y 
                x = y
                y = remainder
            return x
        
        g = gcd(x,y)
        #print("gcd: ", g)
        if g == 0:
            return z == 0
        
        return (x+y) >= z and z % g == 0 