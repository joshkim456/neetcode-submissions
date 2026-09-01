from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()

        taken = 0

        for p in prerequisites:
            indeg[p[0]] += 1
            adj[p[1]].append(p[0])
        
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            taken += 1
            s = q.popleft()

            for nei in adj[s]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
            
        return taken == numCourses
