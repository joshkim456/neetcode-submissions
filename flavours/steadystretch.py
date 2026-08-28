from typing import List
from collections import deque

class Solution:
    def steadyStretch(self, nums: List[int], limit: int) -> int:
        minD = deque()
        maxD = deque()

        ans = 0

        l = 0

        for r in range(len(nums)):
            while minD and nums[r] < nums[minD[-1]]:
                minD.pop()
            while maxD and nums[r] > nums[maxD[-1]]:
                maxD.pop()
            
            minD.append(r)
            maxD.append(r)
            
            while nums[maxD[0]] - nums[minD[0]] > limit:
                if minD[0] == l:
                    minD.popleft()
                if maxD[0] == l:
                    maxD.popleft()
                l += 1

            ans = max(ans, r-l+1)
            
        return ans