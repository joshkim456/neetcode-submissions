# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.total = 0
        
        def traverse(node, maximum):
            if not node:
                return None
            
            if node.val >= maximum:
                self.total += 1
                maximum = node.val
            
            traverse(node.left, maximum)
            traverse(node.right, maximum)
        
        traverse(root, float('-inf'))

        return self.total
