from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                    
                if i == 0:
                    ans.append(node.val)

        return ans