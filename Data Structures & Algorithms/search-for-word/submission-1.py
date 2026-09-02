class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            if visited[r][c]: return False
            if board[r][c] != word[i]: return False

            visited[r][c] = True

            found = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            visited[r][c] = False

            return found

        for r in range(rows):
            for c in range(cols):
                found = dfs(r, c, 0)
                if found: return True
        
        return False

        


        