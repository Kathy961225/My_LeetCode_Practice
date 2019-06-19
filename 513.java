class Solution {
    private int maxDepth;
    private int maxDepthVal;

    private void findBottom(TreeNode node, int depth) {
        // if node is null, stop
        if (node == null) return;

        // increment depth by one
        depth++;

        // if this is a leaf node and its depth is deeper than
        // the saved maximum depth, replace the value
        if (node.left == null && node.right == null && depth > maxDepth) {
            maxDepth    = depth;
            maxDepthVal = node.val;
        // Otherwise, recursively go down the left and right branches
        } else {
            if (node.left  != null) findBottom(node.left, depth);
            if (node.right != null) findBottom(node.right, depth);
        }
    }

    public int findBottomLeftValue(TreeNode root) {
        maxDepth    = 0;
        maxDepthVal = root.val;
        findBottom(root.left, 0);
        findBottom(root.right, 0);
        return maxDepthVal;
    }
}