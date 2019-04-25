# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None: 
            return []
        
        import collections
        
        temp = collections.deque()
        
        temp.append((root, 0))
        
        res = collections.defaultdict(list)
        
        while temp:
            node, level = temp.popleft()
            res[level].append(node.val)
            level += 1
            if node.left:
                temp.append((node.left, level))
            if node.right:
                temp.append((node.right, level))
                
        for i in range(0, level):
            if (i%2) == 1:
                res[i].reverse()
                
        return res.values()