from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        check = root
        heights = {}
        max_length = 0
        # find the node such that the sum of the heights of the left and right trees is maximized
        while check:
            height_left = self.height(check.left, heights) 
            height_right = self.height(check.right, heights)

            if height_left + height_right >= max_length:
                max_length = height_left + height_right
            else:
                break

            check = check.left if height_left > height_right else check.right

        return max_length


    def height(self, root: Optional[TreeNode], heights):
        """
        returns and saves number of nodes in tree at root; # nodes = # edges + 1
        """
        if not root:
            return 0
        
        if root in heights:
            return heights[root]

        height_left = heights[root.left] if root.left in heights else self.height(root.left, heights)
        height_right = heights[root.right] if root.right in heights else self.height(root.right, heights)

        height = max(height_left, height_right) + 1
        heights[root] = height

        return height

print('\033c')
solution = Solution()
a = TreeNode(1)

print(solution.diameterOfBinaryTree(a))