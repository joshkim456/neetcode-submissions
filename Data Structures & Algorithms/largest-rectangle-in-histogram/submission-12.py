class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        heights += [0]

        for r in range(len(heights)):
            start = r
            while stack and stack[-1][1] > heights[r]:
                index, height = stack.pop()
                ans = max(ans, height * (r - index))
                start = index
            stack.append((start, heights[r]))
        
        return ans

                
        
