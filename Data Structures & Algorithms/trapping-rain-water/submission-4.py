class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights)-1
        Lmax = heights[l]
        Rmax = heights[r]

        res = 0

        while l < r:
            if Lmax < Rmax:
                l += 1
                Lmax = max(Lmax, heights[l])
                res += Lmax - heights[l]
            else:
                r -= 1
                Rmax = max(Rmax, heights[r])
                res += Rmax - heights[r]
        return res