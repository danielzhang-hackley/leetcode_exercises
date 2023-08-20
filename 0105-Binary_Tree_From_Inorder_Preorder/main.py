from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # node = TreeNode(val=val, 
        #   left=buildTree(preorder till right, inorder left of node), 
        #   right=buildTree(preorder starting at right, inorder right of node)
        # )
        if not preorder:
            return None

        print(preorder, inorder)
        node_val = preorder[0]
        node_inorder_idx = inorder.index(node_val)

        return TreeNode(
            node_val, 
            self.buildTree(preorder[1:node_inorder_idx+1], inorder[:node_inorder_idx]), 
            self.buildTree(preorder[node_inorder_idx+1:], inorder[node_inorder_idx+1:])
        )
    
print('\033c')
Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])