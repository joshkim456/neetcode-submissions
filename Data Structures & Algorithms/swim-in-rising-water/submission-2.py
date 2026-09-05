import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]
        seen = set()

        rows, cols = len(grid), len(grid[0])

        while h:
            height, r, c = heapq.heappop(h)
            if (r, c) in seen: continue

            seen.add((r, c))

            if r == rows-1 and c == cols-1: return height

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(h, (max(height, grid[nr][nc]), nr, nc))
        
                
