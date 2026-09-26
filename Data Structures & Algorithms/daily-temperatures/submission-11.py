class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        output = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[r]:
                index = s.pop()
                output[index] = r - index
            s.append(r)
        return output