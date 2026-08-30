# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def traverse(node):
            if not node:
                res.append("N")
                return None
            
            res.append(str(node.val))
            
            traverse(node.left)
            traverse(node.right)
        traverse(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        self.cursor = 0

        def build():
            token = tokens[self.cursor]
            self.cursor += 1
            if token == "N":
                return None

            node = TreeNode(token)
            node.left = build()
            node.right = build()

            return node
        
        return build()

            
