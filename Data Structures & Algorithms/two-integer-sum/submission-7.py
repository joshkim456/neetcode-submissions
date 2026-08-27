class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            req = target - n
            if req in seen:
                return [seen[req], i]
            
            seen[n] = i