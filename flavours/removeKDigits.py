from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for r in range(len(num)):
            while stack and stack[-1] > num[r] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[r])

        while k > 0:
            stack.pop()
            k -= 1
        

        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"        
        
        



        

