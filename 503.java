class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] s = new int[nums.length];
        int[] res = new int[nums.length];
        int top = -1;
        for (int i = 2 * nums.length - 1; i >= 0; i--) {
            while (top != -1 && nums[i % nums.length] >= s[top]) {
                top--;
            }
            if (top == -1) {
                res[i % nums.length] = -1;
            } else {
                res[i % nums.length] = s[top];
            }
            s[++top] = nums[i % nu ms.length];
        }
        return res;
    }
}