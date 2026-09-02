from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        d = deque()

        p = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            p[i+1] = p[i] + x
        best = (float('-inf'))
        
        for j in range(len(nums)+1):
            while d and p[j] - p[d[0]] >= k:
                best = min(best, j - d.popleft())
            while d and p[d[-1]] >= p[j]:
                d.pop()
            d.append(j)
        return best



