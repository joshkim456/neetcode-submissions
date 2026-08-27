from typing import List

class Solution:
    def tallestElsewhere(self, heights: List[int]) -> List[int]:
        prefix = [0] * len(heights)
        suffix = [0] * len(heights)

        for i in range(len(heights)):
            prefix[i] = max(prefix[i-1] if i > 0 else -10000000000, heights[i])
        
        for i in range(len(heights)-1, -1, -1):
            suffix[i] = max(suffix[i+1] if i < len(heights)-1 else -10000000000, heights[i])
        
        ans = [0] * len(heights)

        for i in range(len(heights)):
            ans[i] = max(prefix[i-1] if i > 0 else -10000000000, suffix[i+1] if i < len(heights)-1 else -10000000000)
        
        return ans
        
        