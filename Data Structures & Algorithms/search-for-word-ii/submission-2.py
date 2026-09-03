class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            cur = trie.root
            for letter in word:
                if letter in cur.children:
                    cur = cur.children[letter]
                else:
                    cur.children[letter] = TrieNode()
                    cur = cur.children[letter]
            cur.word = word

        output = []
        rows, cols = len(board), len(board[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if visited[r][c]: return
            
            letter = board[r][c]
            if letter not in node.children:
                return
            node = node.children[letter]

            if node.word != "":
                output.append(node.word)
                node.word = ""

            visited[r][c] = True
            dfs(r-1, c, node)
            dfs(r+1, c, node)
            dfs(r, c-1, node)
            dfs(r, c+1, node)

            visited[r][c] = False
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)
        return output

            

            

        


