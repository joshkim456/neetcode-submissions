class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                i = stack.pop()
                output[i] = r - i
            stack.append(r)

        return output