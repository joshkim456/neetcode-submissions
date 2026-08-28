from typing import List

class Solution:
    def nextTaller(self, nums: List[int]) -> List[int]:
        stack = []

        ans = [-1] * len(nums)

        for r in range(len(nums)):
            while stack and nums[r] > nums[stack[-1]]:
                ans[stack.pop()] = nums[r]
            stack.append(r)
        return ans
