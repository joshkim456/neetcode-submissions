# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def trackBiggest(node, biggest):
            if not node:
                return None
            
            if node.val >= biggest:
                biggest = node.val
                self.ans += 1
            
            trackBiggest(node.left, biggest)
            trackBiggest(node.right, biggest)
        
        trackBiggest(root, root.val)
        return self.ans
