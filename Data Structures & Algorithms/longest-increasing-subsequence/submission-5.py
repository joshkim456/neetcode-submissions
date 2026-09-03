class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * (len(nums))
        dp[0] = 1
        for i in range(1, len(dp)):
            dp[i] = 1 + max((dp[j] for j in range(0, i) if nums[j] < nums[i]), default=0)
        
        return max(dp)