class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDag = set()
        posDag = set()

        output = []

        board = [["."] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                output.append(["".join(row) for row in board])
                return

            for col in range(n):
                if col in cols or row - col in negDag or row + col in posDag:
                    continue
                
                cols.add(col)
                negDag.add(row-col)
                posDag.add(row+col)

                board[row][col] = "Q"

                dfs(row+1)

                cols.remove(col)
                negDag.remove(row-col)
                posDag.remove(row+col)

                board[row][col] = "."
        
        dfs(0)
        
        return output