class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in pairs:
                if not stack or stack[-1] != pairs[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        return not stack
