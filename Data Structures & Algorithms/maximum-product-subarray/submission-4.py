class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        curMax = curMin = nums[0]
        res = float('-inf')

        for i in range(1, len(nums)):
            temp = curMax
            curMax = max(nums[i] * curMax, nums[i] * curMin, nums[i])
            curMin = min(nums[i] * temp, nums[i] * curMin, nums[i])

            res = max(res, curMax)

        return res
