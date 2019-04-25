class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = collections.deque()
        
        q.append((root,0))
        res = collections.defaultdict(list)
        while q:
            node, level = q.popleft()
            res[level].append(node.val)
            level += 1
            if node.left:
                q.append((node.left,level))
            if node.right:
                q.append((node.right,level))
        
        return res.values()