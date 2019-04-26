# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return None
        
        res = {}
        
        max_depth = -1
        
        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop()
            
            if node:
            
                max_depth = max(max_depth, depth)
            
                if depth not in res:
                    res[depth] = node.val
                
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
            
        return [res[depth] for depth in range(0, max_depth+1)]