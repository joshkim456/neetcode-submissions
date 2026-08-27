class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dna = [0] * 26
        freqCount = {}

        for s in strs:
            for c in s:
                dna[ord(c) - 97] += 1
            
            if tuple(dna) in freqCount:
                freqCount[tuple(dna)].append(s)
            else:
                freqCount[tuple(dna)] = [s]
            dna = [0] * 26
        
        ans = []
        for dna, l in freqCount.items():
            ans.append(l)
        
        return ans



        