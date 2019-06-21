/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int ans;
    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;
        helper(root, 1);
        return ans;
    }
    
    private int helper(TreeNode root, int level) {
        if (root == null)
            return level - 1;
        int l = helper(root.left, level + 1);
        int r = helper(root.right, level + 1);
        ans = Math.max(ans, l-level+r-level);
        return Math.max(l,r);
        
    }
}