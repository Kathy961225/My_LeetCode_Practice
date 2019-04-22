# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return
        
        path = []
        
        path.append([root, str(root.val)])
        res = 0
        while path:
            node, val = path.pop()
            if node.left:
                path.append((node.left, val+str(node.left.val)))
            if node.right:
                path.append((node.right, val+str(node.right.val)))
            if not node.left and not node.right:
                res += int(val)
                
        return res