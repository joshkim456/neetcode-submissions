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

        def dfs(i, node):
            if i == len(word):
                return node.end
            
            if word[i] == ".":
                
                for letter in node.children:
                    if dfs(i+1, node.children[letter]):
                        return True
                return False
            else:
                if word[i] in node.children:
                    return dfs(i+1, node.children[word[i]])
                else:
                    return False
        
        return dfs(0, self.root)
                
        
