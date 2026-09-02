from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        setList = set(wordList)

        q = deque()
        q.append(beginWord)
        steps = 1

        while q:
            for _ in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return steps
                
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(len(word)):
                        if word[:i] + ch + word[i+1:] in setList:
                            setList.remove(word[:i] + ch + word[i+1:])
                            q.append(word[:i] + ch + word[i+1:])
            steps += 1

        return 0
            
