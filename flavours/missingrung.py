from typing import List

class Solution:
    def longestWithOneGap(self, rungs: List[int]) -> int:
        rungSet = set(rungs)

        ans = 0
        used = False

        for rungs in rungSet:
            m = rungs - 1
            used = False
            length = 0
            
            while True:
                if m in rungSet:
                    length += 1
                    ans = max(ans, length)
                elif not used:
                    length += 1
                    used = True
                else:
                    break
                m += 1

        return ans
