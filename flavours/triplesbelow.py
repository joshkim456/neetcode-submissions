from typing import List

class Solution:
    def countTriples(self, nums: List[int], target: int) -> int:

        nums.sort()
        count = 0

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
                
        return count

