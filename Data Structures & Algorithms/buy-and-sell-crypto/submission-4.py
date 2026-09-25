class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minimum = prices[0]

        for price in prices:
            ans = max(ans, price - minimum)

            minimum = min(minimum, price)
        
        return ans

