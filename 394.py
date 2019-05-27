class Solution {
    public int longestSubstring(String s, int k) {
        if(s==null) {
            return 0;
        }
        return helper(s, 0, s.length()-1, k);
    }
    private int helper(String s, int start, int end, int k) {
        int[] count = new int[26];
        for(int j=start; j<=end ; j++) {
            count[s.charAt(j)-'a'] +=1;
        }
       
        for(int i=start; i<=end; i++) {
            if(count[s.charAt(i)-'a']> 0 && count[s.charAt(i)-'a']<k) { //if char has less than k count, recursively look for left and right substrings
                return Math.max(helper(s, start, i-1, k), helper(s, i+1, end, k));
            }
        }
        return end-start+1; 
    }
}