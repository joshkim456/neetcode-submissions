import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = [(0, 0)]
        seen = set()
        total = 0

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(seen) < len(points):
            cost, i = heapq.heappop(h)
            if i in seen:
                continue
            
            seen.add(i)
            total += cost

            for j in range(len(points)):
                heapq.heappush(h, (dist(i, j), j))
        
        return total
