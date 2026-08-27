class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                ans = max(prices[j] - prices[i], ans)
        
        return ans