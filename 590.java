class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> list = new ArrayList<>();
        postorder(root, list);
        return list;
    }

    private void postorder(Node node, List<Integer> list) {
        if (node != null) {
            for (Node n : node.children) {
                postorder(n, list);
            }
            list.add(node.val);
        }
    }
}