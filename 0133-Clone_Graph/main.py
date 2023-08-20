from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        clone = Node(node.val, node.neighbors)
        checked = set([node])
        queue = deque([node])

        while queue:
            for _ in range(len(queue)):
                n = queue.popleft()
                for neighbor in n.neighbors:
                    if neighbor not in checked:
                        checked.add(neighbor)
                        queue.append(neighbor)
                        n.neighbors.append(neighbor)
        
        return clone
