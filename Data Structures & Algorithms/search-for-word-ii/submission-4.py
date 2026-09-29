class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        pt = PrefixTrie()

        for word in words:
            cur = pt.root
            for letter in word:
                if letter in cur.children:
                    cur = cur.children[letter]
                else:
                    cur.children[letter] = TrieNode()
                    cur = cur.children[letter]
            cur.word = word

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        output = []
        
        def floodfill(r, c, cur):
            if r < 0 or r >= rows or c < 0 or c >= cols: return 
            if visited[r][c]: return 

            if board[r][c] in cur.children:
                cur = cur.children[board[r][c]]

                if cur.word:
                    output.append(cur.word)
                    cur.word = None
                
                visited[r][c] = True
                floodfill(r, c+1, cur)
                floodfill(r, c-1, cur)
                floodfill(r+1, c, cur)
                floodfill(r-1, c, cur)
                visited[r][c] = False
            else:
                return

        for r in range(rows):
            for c in range(cols):
                floodfill(r, c, pt.root)
        
        return output



                