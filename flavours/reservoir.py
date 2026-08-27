from typing import List

class Solution:
    def reservoir(self, heights: List[int]) -> int:
        prefixMax = [0]*len(heights)
        suffixMax = [0]*len(heights)

        for i in range(len(heights)):
            prefixMax[i] = max(prefixMax[i-1] if i > 0 else 0, heights[i])
        
        for i in range(len(heights)-1, -1, -1):
            suffixMax[i] = max(suffixMax[i+1] if i < len(heights)-1 else 0, heights[i])

        ans = 0
        for i in range(len(heights)):
            left = prefixMax[i-1] if i > 0 else 0
            right = suffixMax[i+1] if i < len(heights)-1 else 0

            ans += max(0, min(left, right) - heights[i])
        
        return ans

