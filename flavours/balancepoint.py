from typing import List

class Solution:
    def balancePoint(self, nums: List[int]) -> int:

        total = sum(nums)
        leftTotal = 0

        for i in range(len(nums)):
            leftTotal += nums[i-1] if i > 0 else 0
            rightTotal = total - leftTotal - nums[i]

            if leftTotal == rightTotal:
                return i

        return -1