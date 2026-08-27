class Solution:
    def trap(self, heights: List[int]) -> int:
        prefix = [0]*len(heights)
        suffix = [0]*len(heights)
    
        for i in range(len(heights)):
            prefix[i] = max(prefix[i-1] if i > 0 else 0, heights[i])
        for i in range(len(heights)-1, -1, -1):
            suffix[i] = max(suffix[i+1] if i < len(heights)-1 else 0, heights[i])

        ans = 0
        for i in range(len(heights)):
            left = prefix[i-1] if i > 0 else 0
            right = suffix[i+1] if i < len(heights)-1 else 0
            
            ans += max(0, min(left, right) - heights[i])
        
        return ans