from typing import List

class Solution:
    def longestArc(self, marks: List[int], m: int) -> int:
        markSet = set(marks)

        ans = 0

        if len(markSet) == m:
            return m

        for mark in markSet:
            if ((mark - 1) if mark > 0 else m-1) not in markSet:
                length = 1
                while (mark + length) % m in markSet:
                    length += 1
                ans = max(ans, length)
        
        return ans
                

