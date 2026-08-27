class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dna = [0]*26

        #hashmap: keys = dna, values = words

        hashmap = {}

        for s in strs:
            dna = [0]*26

            for letter in s:
                dna[ord(letter)-97] += 1
            
            if tuple(dna) in hashmap:
                hashmap[tuple(dna)].append(s)
            else:
                hashmap[tuple(dna)] = [s]
            
        buckets = []

        for bucket, values in hashmap.items():
            buckets.append(list(values))
        
        return buckets




        