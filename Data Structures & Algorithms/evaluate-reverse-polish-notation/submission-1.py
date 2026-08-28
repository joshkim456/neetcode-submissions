class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token not in "+*/-":
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == "+":
                    stack.append(right + left)
                elif token == "*":
                    stack.append(right * left)
                elif token == "-":
                    stack.append(left - right)
                elif token == "/":
                    stack.append(int(left / right))
        
        return int(stack[0])
                