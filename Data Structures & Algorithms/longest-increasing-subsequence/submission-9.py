class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(1, len(nums)):
            dp[i] = 1 + max((dp[j] for j in range(i) if nums[i] > nums[j]), default=0)
        
        return max(dp)