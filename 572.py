class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tree1 = self.preorder(s)
        tree2 = self.preorder(t)
        return tree2 in tree1
    
    def preorder(self, t: TreeNode):
        if t == None:
            return "None"
        return "#"+ str(t.val) + " " + self.preorder(t.left) + " " + self.preorder(t.right)