# Definition for a binary tree node.
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '# '
        
        chars = str(root.val) + ' '
        return chars + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '# ' or data is None:
            return None
        
        data = data.split()

        root = cur = TreeNode(int(data[0]))
        checked = defaultdict(int)  # record if right/left has been checked
        checked[cur] = 0
        s = deque([cur])  # should contain nodes?

        for node_val in data[1:]:
            while checked[cur] == 2:
                # remove nodes that are checked on both sides
                s.pop()
                cur = s[-1]

            if node_val == '#':
                checked[cur] += 1
                continue

            node_val = int(node_val)
            prev = cur

            if checked[cur] == 0:
                cur.left = TreeNode(node_val)
                cur = cur.left
            else:
                cur.right = TreeNode(node_val)
                cur = cur.right
            
            checked[prev] += 1
            s.append(cur)

        return root




            

        


print('\033c')
# Your Codec object will be instantiated and called as such:
n4 = TreeNode(4)
n5 = TreeNode(5)
n3 = TreeNode(3, n4, n5)
n2 = TreeNode(2)
root = TreeNode(1, left=n2, right=n3)

ser = Codec()
deser = Codec()
print(ser.serialize(root))
deser.deserialize(ser.serialize(root))

# ans = deser.deserialize(ser.serialize(root))