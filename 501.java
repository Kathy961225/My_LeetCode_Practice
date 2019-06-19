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
    private List<Integer> res = new ArrayList<>();
    private int most_times = 0;        
    private int pre = 0;
    private int times = 0;
    public int[] findMode(TreeNode root) {
        most_times = 0;        
        int pre = 0;
        int times = 0;
        preorder(root);
        
        System.out.println(res);
        int[] ret = new int[res.size()];
        for (int i = 0; i < ret.length; i++) {
            ret[i] = res.get(i);
        }
        return ret;

    }
    
    private void preorder(TreeNode node) {
        if (node == null)
            return;
        preorder(node.left);
        if (!res.isEmpty() && node.val != pre)
            times = 0;
        times += 1;
        if (times == most_times) {
            res.add(node.val);
            System.out.println(res);
        } else if (times > most_times) {
            most_times = times;
            res.clear();
            System.out.println(res);
            res.add(node.val);
            System.out.println(res);
        }
        pre = node.val;
        
        preorder(node.right);
    }
}