# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False
        
        path = []
        
        path.append((root, 0))
        
        while path:
            node, val = path.pop()
            if node.left:
                path.append((node.left, node.val+val))
            if node.right:
                path.append((node.right, node.val+val))
            if not node.right and not node.left:
                if val+node.val == sum:
                    return True
        return False