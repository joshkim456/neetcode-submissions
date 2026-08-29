# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2

        dummy = ListNode()
        cur = dummy

        while l or r:
            if not l and r:
                cur.next = r
                cur = cur.next
                r = r.next
            elif l and not r:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                if l.val < r.val:
                    cur.next = l
                    cur = cur.next
                    l = l.next
                else:
                    cur.next = r
                    cur = cur.next
                    r = r.next
        return dummy.next
                