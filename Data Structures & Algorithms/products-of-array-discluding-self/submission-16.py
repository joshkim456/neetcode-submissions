class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums)+1)
        suffix = [1] * (len(nums)+1)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        output = []

        for i in range(len(prefix)-1):
            output.append(prefix[i]*suffix[i+1])
        
        return output