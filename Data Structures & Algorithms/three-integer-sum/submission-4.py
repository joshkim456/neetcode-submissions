class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = 1
        k = len(nums)-1

        nums.sort()

        ans = set()

        for i in range(0, len(nums)):           
            j = i+1
            k = len(nums)-1

            while j < k:
                if(nums[j] + nums[k] > -nums[i]):
                    k -= 1
                elif(nums[j] + nums[k] < -nums[i]):
                    j += 1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
        
        return [list(t) for t in ans]
