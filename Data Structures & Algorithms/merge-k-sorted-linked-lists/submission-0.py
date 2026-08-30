# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        
        counter = 0
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, counter, l))
                counter += 1
        
        dummy = ListNode()
        cur = dummy
        
        while h:
            toAdd = heapq.heappop(h)[2]
            cur.next = toAdd
            cur = cur.next

            if toAdd.next:
                heapq.heappush(h, (toAdd.next.val, counter, toAdd.next))
                counter += 1

        return dummy.next