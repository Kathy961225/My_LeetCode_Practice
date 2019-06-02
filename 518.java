class Solution {
    public int change(int amount, int[] coins) {
        int[] answer = new int[amount + 1];
        answer[0] = 1;
        for(int coin : coins){
            for(int i=1; i<=amount; i++){
                if(coin <= i)
                    answer[i] += answer[i - coin];
            }
        }
        return answer[amount];
    }
}