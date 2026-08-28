from typing import List
from collections import deque

class Solution:
    def tideMarks(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []

        for r in range(len(nums)):
            while d and nums[r] < nums[d[-1]]:
                d.pop()
            d.append(r)
            if d[0] <= r - k:
                d.popleft()
            if r >= k - 1:
                ans.append(nums[d[0]])
        return ans