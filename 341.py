class NestedIterator(object):

def __init__(self, nestedList):
    """
    Initialize your data structure here.
    :type nestedList: List[NestedInteger]
    """
    self.stack = []
    self.unnest(nestedList)

def unnest(self, nestedList):
    self.stack.extend(nestedList[::-1])

def next(self):
    """
    :rtype: int
    """
    return self.stack.pop().getInteger()

def hasNext(self):
    """
    :rtype: bool
    """
    while self.stack and not self.stack[-1].isInteger():
        self.unnest(self.stack.pop().getList())
    return self.stack