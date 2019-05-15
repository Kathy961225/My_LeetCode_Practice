class Solution(object):
    cnt=0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None:
            return 0
        self.path(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        return self.cnt
        
    def path(self,root,sum):
        if root==None:
            return
        if root.val==sum:
            self.cnt+=1
        self.path(root.left,sum-root.val)
        self.path(root.right,sum-root.val)