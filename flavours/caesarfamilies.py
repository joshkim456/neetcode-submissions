from typing import List

class Solution:
    def groupShifted(self, words: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in words:
            label = []
            for letter in word:
                label.append((ord(letter) - ord(word[0])) % 26)
            
            key = tuple(label)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
            
        ans = []
        for key, value in hashmap.items():
            ans.append(value)
        
        return ans