class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxDist = 0

        for i in range(len(nums)):
            if maxDist < i:
                return False
            
            maxDist = max(maxDist, i + nums[i])
        return True
