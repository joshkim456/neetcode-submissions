import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            stone1 = -heapq.heappop(h)
            stone2 = -heapq.heappop(h)

            if stone1 != stone2:
                heapq.heappush(h, -abs(stone1 - stone2))
        
        if len(h):
            return -h[0]
        else:
            return 0
