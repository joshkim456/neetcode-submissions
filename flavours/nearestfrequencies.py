from typing import List
import heapq

class Solution:
    def nearest(self, nums: List[int], t: int, k: int) -> List[int]:
        h = []

        for num in nums:
            diff = abs(num - t)

            if(len(h) < k):
                heapq.heappush(h, (-diff, -num))
            elif (-diff, -num) > h[0]:
                heapq.heappushpop(h, (-diff, -num))
        
        ans = []

        for pair in sorted(h, reverse=True):
            ans.append(-pair[1])
        return ans

