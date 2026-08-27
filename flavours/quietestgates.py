from typing import List

class Solution:
    def quietestGates(self, gates: List[int], k: int) -> List[int]:
        freq = {}

        for gate in gates:
            if gate in freq:
                freq[gate] += 1
            else:
                freq[gate] = 1
            
        buckets = [[] for _ in range(len(gates)+1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        i = 0
        ans = []

        while i < len(buckets) and len(ans) < k:
            for gate in buckets[i]:
                ans.append(gate)
                if len(ans) == k:
                    return ans
            i += 1

        return ans