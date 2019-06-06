https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/293341/Python3-Easy-to-understand


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tree = preorder.split(',')
        stack = []
        
        for node in tree:
            if not stack or node != '#':
                stack.append(node)
            else:
                while stack and stack[-1] == '#':
                    stack.pop()
                    if not stack:
                        return False
                    else:
                        stack.pop()
                stack.append('#')
        
        return len(stack) == 1 and stack[-1] == '#'