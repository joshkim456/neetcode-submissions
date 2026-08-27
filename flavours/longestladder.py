from typing import List

class Solution:
    def longestLadder(self, nums: List[int], d: int) -> int:
        numSet = set(nums)

        ans = 0

        for num in numSet:
            if num - d not in numSet:
                length = 1
                while num + length * d in numSet:
                    length += 1
                ans = max(ans, length)
            
        return ans