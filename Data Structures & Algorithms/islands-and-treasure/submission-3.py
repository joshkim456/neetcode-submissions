from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()

            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))
        

