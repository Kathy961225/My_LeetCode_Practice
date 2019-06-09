    private Map<TreeNode, Integer> map = new HashMap<>();
    
    public int rob(TreeNode root) {
        if (map.containsKey(root)) {
            return map.get(root);
        }
        
        int result = Math.max(robFrom(root), robNext(root));
        map.put(root, result);
        return result;
    }
    
    private int robFrom(TreeNode node) {
        if (node == null) {
            return 0;
        }
        
        return node.val + robNext(node.left) + robNext(node.right);
    }
    
    private int robNext(TreeNode node) {
        if (node == null) {
            return 0;
        }
        
        return rob(node.left) + rob(node.right);
    }
}