def __init__(self, root):
    """
    :type root: TreeNode
    """
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left

def next(self):
    """
    @return the next smallest number
    :rtype: int
    """
    ret_node = self.stack.pop(-1)
    if ret_node.right:
        node = ret_node.right
        while node:
            self.stack.append(node)
            node = node.left
    return ret_node.val

def hasNext(self):
    """
    @return whether we have a next smallest number
    :rtype: bool
    """
    return self.stack