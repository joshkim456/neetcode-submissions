class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
            else:
                cur.children[letter] = TrieNode()
                cur = cur.children[letter]
        cur.end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.end
            
            if word[i] == ".":
                for letter in node.children:
                    if dfs(node.children[letter], i+1):
                        return True
                return False
            elif word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            else:
                return False
        
        return dfs(self.root, 0)

            


