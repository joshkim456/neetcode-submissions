class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        output = []
        nums.sort()

        while i < len(nums):
            j = i+1
            k = len(nums)-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        return output
                
                