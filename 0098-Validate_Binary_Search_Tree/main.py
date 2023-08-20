from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, side):
            """
            search for max if left, search for min if right
            returns (is_valid, min or max)
            """
            if not root:
                return True, None
            
            l_valid, l_extr = helper(root.left, 'left')
            r_valid, r_extr = helper(root.right, 'right')

            if not l_extr: l_extr = root.val
            if not r_extr: r_extr = root.val


            return l_valid and r_valid and l_extr <= root.val and r_extr >= root.val, \
                   r_extr if side == 'left' else l_extr
        
        l_valid, l_extr = helper(root.left, 'left')
        r_valid, r_extr = helper(root.right, 'right')

        return l_valid and r_valid and \
               (not l_extr or l_extr < root.val) and \
               (not r_extr or r_extr > root.val)



print('\033c')
a = TreeNode(1)
c = TreeNode(3)
b = TreeNode(2, left=a, right=c)
print(Solution().isValidBST(TreeNode(0)))