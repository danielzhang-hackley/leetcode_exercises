from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        stack = [root]

        while len(stack) > 0:
            node = stack.pop()

            temp = node.right
            node.right = node.left
            node.left = temp

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root
