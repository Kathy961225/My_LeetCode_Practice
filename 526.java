class Solution {
    int count = 0;
    public int countArrangement(int N) {
        boolean[] visited = new boolean[N+1];
        helper(N, 1, visited);
        return count;
    }
    
    private void helper(int N, int pos, boolean[] visited) {
        if (pos > N)
            ++count;
        
        for (int i=1; i<= N; ++i) {
            if (!visited[i] && (pos % i == 0 || i % pos == 0)) {
                visited[i] = true;
                helper(N, pos+1, visited);
                visited[i] = false;
            }
        }
    }
}