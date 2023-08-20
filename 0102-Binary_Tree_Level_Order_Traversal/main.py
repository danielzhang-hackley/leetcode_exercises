from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []

        temp_queue = []
        temp_ans = []

        while queue:
            while queue:
                node = queue.popleft()
                if node:
                    temp_ans.append(node.val)
                    temp_queue.append(node.left), temp_queue.append(node.right)
            queue.extend(temp_queue)
            ans.append(temp_ans)
            temp_queue = []; temp_ans = []

        return ans[:-1]

print('\033c')

n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20, n15, n7)
n9 = TreeNode(9)
n3 = TreeNode(3, n9, n20)

solution = Solution()
print(solution.levelOrder(TreeNode(1)))
