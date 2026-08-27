from typing import List
import heapq

class Solution:
    def minRunways(self, flights: List[List[int]]) -> int:
        h = []

        flights.sort()

        for flight in flights:
            if not h or flight[0] < h[0]:
                heapq.heappush(h, flight[1])
            else:
                heapq.heappop(h)
                heapq.heappush(h, flight[1])
        
        return len(h)
