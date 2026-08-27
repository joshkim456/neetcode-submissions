class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = set()

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        return [list(triple) for triple in ans]
