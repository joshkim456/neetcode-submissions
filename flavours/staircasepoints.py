from typing import List

class Solution:
    def longestStaircase(self, points: List[List[int]]) -> int:
        pointSet = set(tuple(p) for p in points)

        ans = 0
        for point in pointSet:
            if (point[0]-1, point[1]-1) not in pointSet:
                length = 1
                while (point[0]+length, point[1]+length) in pointSet:
                    length += 1
                ans = max(ans, length)

        return ans