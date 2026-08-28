class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)

            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if bracket == ")" and top != "(":
                    return False
                if bracket == "]" and top != "[":
                    return False
                if bracket == "}" and top != "{":
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
