class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[-1])

        def rob(nums):
            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = nums[1]
            for i in range(len(nums)):
                for j in range(0, i-1):
                    dp[i] = max(dp[i], dp[j] + nums[i])
            return max(dp)
        
        return max(rob(nums[1:]), rob(nums[:-1]))
            

[2, 9, 0, 0, 0]
[2, 9, 8, 3, 6]