class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums, lambda a, b: a*b))
        suffix = list(accumulate(nums[::-1], lambda a, b: a*b))[::-1]

        ans = []

        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums)-1 else 1

            ans.append(left * right)
        
        return ans

