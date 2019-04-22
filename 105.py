# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(inorder) == 1:
            root = TreeNode(preorder[0])
            return root
        
        node_val = preorder[0]
        root = TreeNode(node_val)
        index = inorder.index(node_val)
        inorder_left = inorder[0:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root