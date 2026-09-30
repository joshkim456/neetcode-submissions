from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        q = deque()
        adj = [[] for _ in range(numCourses)]
        indeg = [0]*numCourses

        for p in prerequisites:
            indeg[p[0]] += 1
            adj[p[1]].append(p[0])
        
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            output.append(node)

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        return output if len(output) == numCourses else []
            


