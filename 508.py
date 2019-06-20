def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.sums = collections.defaultdict(int)
        self.dfs(root)
        res = []
        max_freq = max(self.sums.values())
        for stree_sum in self.sums:
            if self.sums[stree_sum] == max_freq:
                res.append(stree_sum)
        return res
        
    def dfs(self, node):
        if node:
            left = self.dfs(node.left)
            right = self.dfs(node.right)
            self.sums[right + left + node.val] += 1
            return right + left + node.val
        return 0