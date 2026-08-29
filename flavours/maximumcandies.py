from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo = 0
        hi = max(candies)

        def served(amount):
            return sum(c // amount for c in candies) >= k

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if served(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
            
