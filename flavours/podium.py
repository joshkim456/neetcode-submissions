from typing import List

class Solution:
    def podium(self, gates: List[int], k: int) -> List[int]:
        freq = {}

        for gate in gates:
            freq[gate] = freq.get(gate, 0) + 1

        buckets = [[] for _ in range(len(gates)+1)]
        
        for key, value in freq.items():
            buckets[value].append(key)
    
        i = len(buckets)-1
        ans = []

        while i >= 0:
            buckets[i].sort()
            for gate in buckets[i]:
                ans.append(gate)
                if len(ans) == k:
                    return ans
            i -= 1
        
        return ans


