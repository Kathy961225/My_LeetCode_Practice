suppose at a point i the array is A[0], A[1], A[2], A[3],..., A[k-1], A[k] then we have :

  f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
  f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k] 
=>f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +       A[k-1]    - k * A[k] 
   = (A[0]   +   A[1]   +   A[2] + ...  +       A[k-1] + k * A[k]) - (k+1) * A[k]
   = sum(Array) - A[k] * array.length
=> f(i+1) = f(i) + sum(Array) -  last element * array.length
so at a point i if we know f(i) then we could easily caculate f(i+1) by the above formula so just go through the array and update the maximum value.
here is my code:

class Solution(object):
    def maxRotateFunction(self, A):
        r = curr = sum(i * j for i,j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r