class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            new = dist.copy()
            for u, v, w in flights:
                if dist[u] + w < new[v]: new[v] = dist[u] + w
            dist = new

        return dist[dst] if dist[dst] != float('inf') else -1