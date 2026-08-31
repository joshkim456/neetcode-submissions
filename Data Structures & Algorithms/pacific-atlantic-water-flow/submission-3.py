class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows, cols = len(heights), len(heights[0])
        
        def floodfill(r, c, seen, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if (r, c) in seen: return
            if heights[r][c] < prev: return

            seen.add((r, c))

            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                floodfill(nr, nc, seen, heights[r][c])
        
        #floodfill for pac, floodfill for atl
        #return the list of the intersection of the remaining sets
    
        for r in range(rows):
            floodfill(r, 0, pac, float('-inf'))
            floodfill(r, cols-1, atl, float('-inf'))
        
        for c in range(cols):
            floodfill(0, c, pac, float('-inf'))
            floodfill(rows - 1, c, atl, float('-inf'))
        
        return [[r, c] for r, c in pac & atl]
        
        


            
            


