from typing import List

class Solution:
    def countIslandShapes(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        islands = set()

        def floodFill(label, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if visited[r][c]: return
            if grid[r][c] == 0: return
        
            visited[r][c] = True
            label.append([r, c])

            floodFill(label, r+1, c)
            floodFill(label, r-1, c)
            floodFill(label, r, c+1)
            floodFill(label, r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                label = []
                if grid[r][c] == 1 and not visited[r][c]:
                    floodFill(label, r, c)

                    minR = min(cell[0] for cell in label)
                    minC = min(cell[1] for cell in label)

                    for indices in label:
                        indices[0] -= minR
                        indices[1] -= minC
                    
                    index = tuple(sorted(tuple(cell) for cell in label))
                    islands.add(index)
        
        return len(islands)
                





