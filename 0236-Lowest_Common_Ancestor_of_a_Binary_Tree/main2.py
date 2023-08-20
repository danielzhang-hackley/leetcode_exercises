"""
Treat inputs p and q as integers because leetcode is fucking stupid bitch-ass hoe
"""

from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return self.val, self.left.val if self.left else None, self.right.val if self.right else None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = deque([root])
        parents = defaultdict(list)  # key is node, value is array of parents from top to bottom

        p_found = False
        q_found = False

        while not (p_found and q_found):
            print(s)
            node = s.pop()
            parents[node.val].append(node.val)

            if node.val == p:
                p_found = True
            if node.val == q:
                q_found = True

            if node.left:
                parents[node.left.val].extend(parents[node.val])
                s.append(node.left)
            if node.right:
                parents[node.right.val].extend(parents[node.val])
                s.append(node.right)

        for i in range(min(len(parents[p]), len(parents[q]))):
            if parents[p][i] != parents[q][i]:
                return parents[p][i-1]

        return parents[p][min(len(parents[p]), len(parents[q]))-1]
    

print('\033c')

n7 = TreeNode(7)
n4 = TreeNode(4)
n6 = TreeNode(6)
n2 = TreeNode(2, left=n7, right=n4)
n0 = TreeNode(0)
n8 = TreeNode(8)
n5 = TreeNode(5, left=n6, right=n2)
n1 = TreeNode(1, left=n0, right=n8)
n3 = TreeNode(3, left=n5, right=n1)

n02 = TreeNode(2)
n01 = TreeNode(1, left=n02)

print(Solution().lowestCommonAncestor(n01, 2, 1))