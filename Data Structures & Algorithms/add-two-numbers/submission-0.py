# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        l = l1
        r = l2
        carry = 0

        while l or r or carry:
            s = (l.val if l else 0) + (r.val if r else 0) + carry
            carry, digit = divmod(s, 10)

            new = ListNode(digit)
            cur.next = new
            cur = cur.next
            
            l = l.next if l else None
            r = r.next if r else None
        
        return dummy.next 
            
            



