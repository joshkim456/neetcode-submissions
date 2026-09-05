import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # loop over queryWithIndex
        # Push while the interval's lo <= q
        # pop while the heap's top's hi < q

        intervals.sort()
        queryWithIndex = []
        for i in range(len(queries)):
            queryWithIndex.append((queries[i], i))
        queryWithIndex.sort()
    

        h = []

        output = [-1] * len(queries)
        j = 0

        for q, i in queryWithIndex:
            while j < len(intervals) and intervals[j][0] <= q:
                width = intervals[j][1] - intervals[j][0] + 1
                heapq.heappush(h, (width, intervals[j][1]))
                j += 1
            
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            if h:
                output[i] = h[0][0]
        
        return output

        
