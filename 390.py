1. if n == 2 * k + 1
At this time, the sequence is 1, 2, 3, 4, ..., 2 * k, 2 * k + 1, delete it from left to right, then we have a new sequence: 2, 4, 6, ..., 2 * k, which is a sequence length of k. Notice that this sequence is indeed the same problem with smaller size!!! As a result, if we treat 2 * k as 1, 2 * k - 2 as 2, ..., 4 as k - 1, 2 as k,
that is,
2 4 6 8 ... 2*k oldid = (k - newid + 1) * 2
to
k k-1 k - 2 k - 3 .... 1 newid

so if we denote the solution for the smaller problem as f(k), then using the relationship between them we could simply obtain the result that

f(n) = (k - f(k) + 1) * 2 = (n / 2 - f(n / 2) + 1) * 2.

2. if n == 2 * k
At this time, the sequence is 1, 2, 3, 4, ..., 2 * k, delete it from left to right, then we have a new sequence: 2, 4, 6, ..., 2 * k, which is a sequence length of k. Since it is in the same format with the case 1. Still we have the same relation:

f(n) = (k - f(k) + 1) * 2 = (n / 2 - f(n / 2) + 1) * 2

As a result, for any n >= 1, we have the relation:

f(n) = (k - f(k) + 1) * 2 = (n / 2 - f(n / 2) + 1) * 2
My codes:

class Solution {
public:
    int lastRemaining(int n) {
        if (n == 1)
            return 1;
        return (((n >> 1) - lastRemaining(n >> 1) + 1) << 1); 
    }
};