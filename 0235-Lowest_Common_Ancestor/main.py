# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = [root]
        q_path = [root]

        while True:
            if p_path[-1].val > p.val:
                p_path.append(p_path[-1].left)
            elif p_path[-1].val < p.val:
                p_path.append(p_path[-1].right)
            else:
                break

        while True:
            if q_path[-1].val > q.val:
                q_path.append(q_path[-1].left)
            elif q_path[-1].val < q.val:
                q_path.append(q_path[-1].right)
            else:
                break

        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]:
                return p_path[i-1]

        return p_path[i]
