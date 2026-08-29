from typing import List

class Solution:
    def priceSpan(self, prices: List[int]) -> List[int]:
        stack = []
        output = [0] * len(prices)

        for r in range(len(prices)):
            while stack and prices[stack[-1]] <= prices[r]:
                stack.pop()
            stack.append(r)
            output[r] = r - stack[-1] if stack else r + 1
        return output
