"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        conversion = {}

        cur = head
        while cur:
            conversion[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            conversion[cur].next = conversion[cur.next] if cur.next else None
            conversion[cur].random = conversion[cur.random] if cur.random else None
            cur = cur.next
        
        return conversion.get(head, None)
    