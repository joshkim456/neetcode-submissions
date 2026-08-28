from typing import List

class Solution:
    def previousShorter(self, heights: List[int]) -> List[int]:
        stack = []
        output = [-1] * len(heights)

        for r in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[r]:
                stack.pop()
            