class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        cur = []
        def dfs(i):
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                piece = s[i:j+1]
                if piece == piece[::-1]:
                    cur.append(piece)
                    dfs(j+1)
                    cur.pop()
        
        dfs(0)
        return res