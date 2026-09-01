class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = float('-inf')
        smallest = 0
        total = 0

        for n in nums:
            total += n
            ans = max(ans, total - smallest)
            smallest = min(smallest, total)
        
        return ans

