class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def floodfill(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if visited[r][c]: return
            if grid[r][c] == "0": return

            visited[r][c] = True

            floodfill(r+1, c)
            floodfill(r-1, c)
            floodfill(r, c+1)
            floodfill(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":
                    count += 1
                    floodfill(r, c)
        
        return count


