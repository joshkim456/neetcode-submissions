import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(h, (-dist, point))
        
        while len(h) > k:
            heapq.heappop(h)
        
        output = []

        for dist, point in h:
            output.append(point)
        
        return output