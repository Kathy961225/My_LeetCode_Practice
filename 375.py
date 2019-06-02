class Solution {
    public int getMoneyAmount(int n) {
        return dfs(new Integer[n + 1][n + 1], 1, n);
    }
    
    int dfs(Integer[][] memo, int left, int right) {
        if (left >= right) return 0;
        if (memo[left][right] != null) return memo[left][right];
        
        int res = Integer.MAX_VALUE;
        for (int i = left; i <= right; ++i) {
            res = Math.min(res, i + Math.max(dfs(memo, left, i - 1), dfs(memo, i + 1, right)));
        }
        memo[left][right] = res;
        return res;
    }
}