# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def fillLevels(node, level):
            if not node:
                return None

            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            
            fillLevels(node.left, level+1)
            fillLevels(node.right, level+1)
        
        fillLevels(root, 0)

        ans = []
        for key, value in levels.items():
            ans.append(value[-1])
        return ans
