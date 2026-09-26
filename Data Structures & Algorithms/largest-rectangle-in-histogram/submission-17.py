class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        ans = 0

        heights = heights + [0]

        for r in range(len(heights)):
            start = r
            while s and s[-1][1] > heights[r]:
                index, height = s.pop()
                ans = max(ans, height * (r-index))
                start = index
            s.append((start, heights[r]))                
        return ans 
