# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxLength = 0

        def depth(node):
            if not node:
                return 0

            l = depth(node.left)
            r = depth(node.right)

            self.maxLength = max(self.maxLength, l + r)
            return 1 + max(l, r)
        depth(root)

        return self.maxLength
