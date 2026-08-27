from typing import List

class Solution:
    def bestStretch(self, nums: List[int], k: int) -> int:
        total = 0
        l = 0
        r = 0
        
        ans = 0
        while r < k:
            total += nums[r]
            r += 1

        ans = total
        
        while r < len(nums):
            total -= nums[l]
            l += 1
            total += nums[r]
            r += 1

            ans = max(ans, total)
        return ans
        
            

