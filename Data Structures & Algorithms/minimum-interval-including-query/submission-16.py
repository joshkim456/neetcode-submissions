import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queryWithIndex = []
        for i in range(len(queries)):
            queryWithIndex.append((queries[i], i))
        queryWithIndex.sort()

        intervals.sort()

        h = []
        i = 0
        output = [-1] * len(queries)

        for q, index in queryWithIndex:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(h, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while h and h[0][1] < q:
                heapq.heappop(h)
            if h:
                output[index] = h[0][0] 
        
        return output