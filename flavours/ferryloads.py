from typing import List

class Solution:
    def ferryTrips(self, weights: List[int], limit: int) -> int:
        weights.sort()

        l = 0
        r = len(weights)-1

        trips = 0

        while l < r:
            if weights[l] + weights[r] > limit:
                trips += 1
                r -= 1
            else:
                trips += 1
                l += 1
                r -= 1
        
        if l == r:
            return trips+1
        else:
            return trips