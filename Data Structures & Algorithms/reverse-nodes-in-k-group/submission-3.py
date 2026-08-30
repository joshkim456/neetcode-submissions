# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # two pointers method, increase until count < k, if r ever reaches None inside, return dummy.next cos it reached end. don't think it will reach None when count == k, because then while loop will terminate
        # once left and right are k apart, you want to now increase left, and reverse
        # and this is all in a loop, while right? 

        dummy = ListNode()
        dummy.next = head

        left = dummy

        while True:
            
            right = left
            count = 0

            while count < k:
                count += 1
                right = right.next
                
                if not right:
                    return dummy.next
            
            groupNext = right.next
            prev = groupNext
            cur = left.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = left.next
            left.next = right
            left = temp



