from typing import List

class Solution:
    def previousTaller(self, heights: List[int]) -> List[int]:
        stack = []
        output = [-1]*len(heights)

        for r in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[r]:
                stack.pop()
            output[r] = stack[-1] if stack else -1
            stack.append(r)
        return output