from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.pre_off = -1

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_idx = {inorder[i]: i for i in range(len(inorder))}
        

        def solve(pre, ino):
            if not pre:
                return None
            
            self.pre_off += 1
            print(pre, ino)
            return TreeNode(
                pre[0], 
                solve(pre[1:val_to_idx[pre[0]]+1], ino[:val_to_idx[pre[0]]]), 
                solve(pre[val_to_idx[pre[0]]+1:], ino[val_to_idx[pre[0]]+1:])
            )
    
        return solve(preorder, inorder)
    
print('\033c')
Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])

"""
[3, 9, 20, 15, 7] [9, 3, 15, 20, 7]
[9] [9]
[20, 15, 7] [15, 20, 7]
[15] [15]
[7] [7]

"""