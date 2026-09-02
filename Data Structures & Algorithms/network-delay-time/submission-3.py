import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        seen = set()
        adj = [[] for _ in range(n+1)]

        for src, dst, time in times:
            adj[src].append((dst, time))

        t = 0
        
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            time, node = heapq.heappop(minHeap)
            
            if node in seen: continue

            seen.add(node)

            t = time

            for nei, timeToNode in adj[node]:
                heapq.heappush(minHeap, (time + timeToNode, nei))
        
        return t if len(seen) == n else -1




