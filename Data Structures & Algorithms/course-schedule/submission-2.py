from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        visited = [False] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pr in prerequisites:
            indeg[pr[0]] += 1
            adj[pr[1]].append(pr[0])
        
        q = deque()

        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()

            visited[node] = True

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return all(visited)



