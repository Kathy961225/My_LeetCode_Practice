https://leetcode.com/problems/poor-pigs/discuss/270377/VERY-EASY-arithmetics%3A-the-right-way-to-ENCODE-the-buckets-(LESS-than-10-lines-beats-100)


{
    if(buckets==1)
        return 0;
    int digits = 1;
    int base = minutesToTest / minutesToDie + 1;
    int timer = base;
    while(buckets>timer)
    {
        timer*=base;
        digits+=1;
    }
    return digits;
}