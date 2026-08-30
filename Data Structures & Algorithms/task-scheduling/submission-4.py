import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        h = [-c for c in counts.values()]
        heapq.heapify(h)
        q = deque()
        time = 0

        while h or q:
            time += 1
            if h:
                maxCount = heapq.heappop(h) + 1
                if maxCount != 0:
                    q.append((maxCount, time+n))
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        return time



