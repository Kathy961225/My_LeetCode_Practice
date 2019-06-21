class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        stack=collections.deque()
        stack.append(root)
        result=[]
        while(stack):
            curr=stack.popleft()
            if(curr):
                result.append(curr.val)
                [stack.appendleft(child) for child in curr.children[::-1]]
        return result