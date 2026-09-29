class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        curMin = nums[0]
        curMax = nums[0]
        ans = float("-inf")

        for i in range(1, len(nums)):
            curMin, curMax = min(nums[i], curMin*nums[i], curMax*nums[i]), max(nums[i], curMin*nums[i], curMax*nums[i])
            ans = max(curMax, ans)
        
        return ans