from typing import List

class Solution:
    def countBlocks(self, positions: List[int]) -> int:
        positionSet = set(positions)

        ans = 0
        for position in positionSet:
            if position - 1 not in positionSet:
                ans += 1
        
        return ans