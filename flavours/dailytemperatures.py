from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []

        output = [0] * len(temps)

        for r in range(len(temps)):
            while stack and temps[r] > temps[stack[-1]]:
                i = stack.pop()
                output[i] = r - i 
            stack.append(r)
        
        return output