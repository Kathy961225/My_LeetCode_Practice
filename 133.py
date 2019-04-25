class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        return clone(node, {})

def clone(node, dict):
    if node not in dict:
        dict[node] = Node(node.val, [])
        for n in node.neighbors:
            dict[node].neighbors.append(clone(n, dict))
    return dict[node]