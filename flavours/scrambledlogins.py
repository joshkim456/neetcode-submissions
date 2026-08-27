from typing import List

class Solution:
    def countEquivalentPairs(self, attempts: List[str]) -> int:
        dna = [0]*26
        hashmap = {}

        for s in attempts:
            for letter in s:
                dna[ord(letter)-97] += 1

            index = tuple(dna)
            
            if index in hashmap: 
                hashmap[index] += 1
            else:
                hashmap[index] = 1
            
        ans = 0
        for dna, value in hashmap.items():
            ans += (value * (value - 1) // 2)
        
        return ans
