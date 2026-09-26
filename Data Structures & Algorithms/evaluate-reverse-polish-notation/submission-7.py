class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token not in "*+-/":
                s.append(token)
            else:
                right = int(s.pop())
                left = int(s.pop())

                if token == "*":
                    s.append(str(left * right))
                elif token == "+":
                    s.append(str(left + right))
                elif token == "-":
                    s.append(str(left - right))
                else:
                    s.append(str(int(left / right)))
            
        return int(s[-1])