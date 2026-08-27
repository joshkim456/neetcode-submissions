from typing import List
import heapq

class Solution:
    def heaviest(self, weights: List[int], k: int) -> List[int]:
        h = []

        for w in weights:
            if len(h) < k:
                heapq.heappush(h, w)
            elif w > h[0]:
                heapq.heappushpop(h, w)
        
        return sorted(h, reverse=True)
