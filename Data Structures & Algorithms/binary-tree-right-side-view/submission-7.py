# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def fillLevel(node, level):
            if not node:
                return None
            
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            
            fillLevel(node.left, level+1)
            fillLevel(node.right, level+1)
        
        fillLevel(root, 0)

        output = []

        for key, value in levels.items():
            output.append(value[-1])
        
        return output


      