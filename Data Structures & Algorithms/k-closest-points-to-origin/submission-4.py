import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for point in points:
            distSq = point[0]*point[0] + point[1]*point[1]

            heapq.heappush(h, (-distSq, point))
            
            if len(h) > k:
                heapq.heappop(h)

        ans = []
        for distSq, point in h:
            ans.append(point)
        return ans
        

