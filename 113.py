# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if not root:
            return 
        
        res = []
        path = []
        
        path.append((root, 0, [root.val]))
        
        while path:
            node, val, cur = path.pop()
            if node.left:
                path.append((node.left, node.val+val, cur+[node.left.val]))
            if node.right:
                path.append((node.right, node.val+val, cur+[node.right.val]))
            if not node.right and not node.left:
                if val+node.val == sum:
                    res.append(cur)
        return res