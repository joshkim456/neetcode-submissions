class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def floodfill(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if board[r][c] != "O": return

            board[r][c] = "T"

            floodfill(r-1, c)
            floodfill(r+1, c)
            floodfill(r, c-1)
            floodfill(r, c+1)
        
        for r in range(rows):
            floodfill(r, 0)
            floodfill(r, cols-1)
        
        for c in range(cols):
            floodfill(0, c)
            floodfill(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                
