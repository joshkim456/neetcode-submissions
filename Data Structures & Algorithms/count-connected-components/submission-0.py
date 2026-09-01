class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)
        
        def dfs(node):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        ans = 0
        for i in range(0, n):
            if i not in visited:
                ans += 1
                dfs(i)
        return ans