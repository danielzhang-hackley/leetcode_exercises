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
        checked = set([clone.val])
        stack = deque([clone])

        while stack:
            n = stack.pop()
            temp_neighbors = []
            for neighbor in n.neighbors:
                temp_neighbors.append(Node(neighbor.val, neighbor.neighbors))
                if neighbor.val not in checked:
                    stack.append(neighbor)
                    checked.add(neighbor.val)
            n.neighbors = temp_neighbors
        return clone

"""    
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return node
"""

print('\033c')

n1 = Node(1)
n2 = Node(2)
n3 = Node(3, [n1, n2])

print(n3.val, id(n3))
for n in n3.neighbors:
    print(n.val, id(n))

solution = Solution()
x = solution.cloneGraph(n3)
print(x.val, id(x))
for n in x.neighbors:
    print(n.val, id(n))



