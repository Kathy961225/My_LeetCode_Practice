from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        temp = deque()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        
        return self.q2.popleft()
        
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0