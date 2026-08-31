class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def floodFill(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return 
            if visited[r][c]: return
            if grid[r][c] == "0": return

            visited[r][c] = True

            floodFill(r, c-1)
            floodFill(r, c+1)
            floodFill(r-1, c)
            floodFill(r+1, c)

        count = 0

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == "1":
                    count += 1
                    floodFill(r, c)
        return count
