class Solution:
    def rob(self, nums: List[int]) -> int:
            if len(nums) <= 2:
                return max(nums)

            def rob(nums):

            
                dp = [0] * len(nums)

                dp[0] = nums[0]
                dp[1] = nums[1]

                for i in range(2, len(nums)):
                    dp[i] = nums[i] + max(dp[j] for j in range(i-1))
                
                return max(dp)
            
            return max(rob(nums[1:]), rob(nums[:len(nums)-1]))
        
        