class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        def hoursNeeded(k):
            total = 0
            for p in piles:
                total += math.ceil(p / k)
            return total

        while lo < hi:
            mid = (lo + hi) // 2

            if hoursNeeded(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
        