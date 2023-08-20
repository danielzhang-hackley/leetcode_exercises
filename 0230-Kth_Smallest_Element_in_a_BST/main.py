from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return []
            
            temp_order = inorder(node.left) + [node] + inorder(node.right)
            return temp_order

        order = inorder(root)
        return order[k-1].val
    
print('\033c')
print(Solution().kthSmallest)