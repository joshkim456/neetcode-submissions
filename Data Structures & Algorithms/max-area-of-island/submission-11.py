class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def floodfill(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return 0
            if visited[r][c]: return 0 
            if grid[r][c] == 0: return 0

            visited[r][c] = True

            return 1 + floodfill(r-1, c) + floodfill(r+1, c) + floodfill(r, c-1) + floodfill(r, c+1)
        
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == 1:
                    maxArea = max(maxArea, floodfill(r, c))
        
        return maxArea
                