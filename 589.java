class Solution {
    private void helper(Node root, List<Integer> output){
        if(root == null) return;
        output.add(root.val);
        if(root.children != null){
            for(Node child : root.children) 
                helper(child, output);
        }
    }
    public List<Integer> preorder(Node root) {
        List<Integer> output = new ArrayList<>();
        helper(root, output);
        return output;
    }
}