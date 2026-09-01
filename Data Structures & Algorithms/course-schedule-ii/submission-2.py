from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            indeg[a] += 1
            adj[b].append(a)
        
        q = deque()

        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
                
        order = []

        while q:
            s = q.popleft()
            order.append(s)

            for nei in adj[s]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if len(order) == numCourses:
            return order
        else:
            return []