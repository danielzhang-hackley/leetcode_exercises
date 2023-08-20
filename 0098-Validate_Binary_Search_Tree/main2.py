from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque([root])
        
        def check_right(node):
            if not node:
                return True
            min_val = float('inf')
            cur = node.right
            while cur:
                if cur.val >= min_val or cur.val <= node.val:
                    return False
                min_val = cur.val
                cur = cur.left
            return True
        
        def check_left(node):
            if not node:
                return True
            max_val = -float('inf')
            cur = node.left
            while cur:
                if cur.val <= max_val or cur.val >= node.val:
                    return False
                max_val = cur.val
                cur = cur.right
            return True
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            if not (check_left(node) and check_right(node)):
                return False
            stack.append(node.left)
            stack.append(node.right)
        
        return True


print('\033c')
a = TreeNode(1)
c = TreeNode(3)
b = TreeNode(2, left=a, right=c)
print(Solution().isValidBST(TreeNode(0)))