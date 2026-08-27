from typing import List

class Solution:
    def groupPatterns(self, words: List[str]) -> List[List[str]]:
        hashmap = {}
        buckets = []

        for word in words:

            mapping = {}
            label = ""
            for i in range(len(word)):
                if word[i] not in mapping:
                    mapping[word[i]] = len(mapping) 

            for letter in word:
                label += chr(mapping[letter] + 97)
            
            if label in hashmap:
                hashmap[label].append(word)
            else:
                hashmap[label] = [word]
        
        for key, bucket in hashmap.items():
            buckets.append(bucket)
        
        return buckets

                
                
