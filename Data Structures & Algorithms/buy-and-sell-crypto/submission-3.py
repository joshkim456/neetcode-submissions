class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minSoFar = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minSoFar)
            minSoFar = min(minSoFar, prices[i])
            
        return ans
