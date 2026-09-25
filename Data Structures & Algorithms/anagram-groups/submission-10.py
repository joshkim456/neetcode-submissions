class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            dna = [0]*128

            for letter in s:
                dna[ord(letter)] += 1
            
            d.setdefault(tuple(dna), []).append(s)

        output = []
        
        for key, value in d.items():
            output.append(value)
        
        return output
            