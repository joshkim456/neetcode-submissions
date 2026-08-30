# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get middle using fast+slow pointers, left heavy
        #get pointers to first half, and second half, then sever first half
        #reverse second half
        #traverse both first and reverse second halfs, and mutate linked list in place
        # temp1 = first.next, temp2 = second.next, first.next = second, second.next = temp1, first = temp1, second = temp2

        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        

