# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def traverse(node):
            if not node:
                return 0
            
            l = max(0, traverse(node.left))
            r = max(0, traverse(node.right))

            self.ans = max(self.ans, node.val + l + r)

            return node.val + max(l, r)
        
        traverse(root)
        return self.ans
            
