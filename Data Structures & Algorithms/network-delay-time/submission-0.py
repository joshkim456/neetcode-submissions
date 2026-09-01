import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        seen = set()
        adj = [[] for _ in range(n+1)]

        t = 0

        for source, target, time in times:
            adj[source].append((target, time))

        heapq.heappush(minHeap, (0, k))

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in seen: continue

            t = time

            seen.add(node)

            for nei, timeToNei in adj[node]:
                heapq.heappush(minHeap, (time+timeToNei, nei))

        return t if len(seen) == n else -1


