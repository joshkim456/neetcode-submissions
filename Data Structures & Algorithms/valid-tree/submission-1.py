class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)
        
        def dfs(node):
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        dfs(0)

        return all(visited) and len(edges) == n-1
