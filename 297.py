# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        from collections import deque
        stack = deque()
        
        if not root:
            return        
        stack.append(root)
        while stack:
            cur_node = stack.popleft()
            if cur_node == None:
                res.append("null")
            else:
                res.append(cur_node.val)
                stack.append(cur_node.left)
                stack.append(cur_node.right)
        
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        root = TreeNode(data[0])
        
        from collections import deque
        stack = deque()
        stack.append(root)
        i = 1
        while stack:
            cur_node = stack.popleft()
            if data[i] == 'null':
                cur_node.left = None
            else:
                cur_node.left = TreeNode(data[i])
                stack.append(cur_node.left)
            
            if data[i+1] == 'null':
                cur_node.right = 'null'
                cur_node.right = None
            else:
                cur_node.right = TreeNode(data[i+1])
                stack.append(cur_node.right)
            i += 2
        return root