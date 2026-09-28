import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(h, -abs(y-x))
        
        return -h[0] if h else 0