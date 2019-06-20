    public int getMinimumDifference(Node root) {
        if(root==null){
            return result;
        }
        result=Integer.MAX_VALUE;
        pre=Integer.MAX_VALUE;
        inOrder(root);
        return result;
    }

    private void inOrder(Node root){
        if(root==null){
            return;
        }
        inOrder(root.left);
        int temp=Math.abs(root.val-pre);
        result=result<temp?result:temp;
        pre=root.val;
        inOrder(root.right);
    }

