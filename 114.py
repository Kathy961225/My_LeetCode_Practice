# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return None
        
        self.tree = []
        
        self.preorder(root)
        cur = root
        for i in range(1, len(self.tree)):
            cur.left = None
            cur.right = self.tree[i]
            cur = cur.right
            
        root.left = None
        
        return root
        
    
    
    
    
    def preorder(self, root):
        if not root:
            return
        self.tree.append(root)
        self.preorder(root.left)
        self.preorder(root.right)