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
        
        clones = {node.val: Node(node.val)}
        stack = deque([node])

        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                clones[n.val].neighbors.append(clones[neighbor.val])

        return clones[node.val]


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



