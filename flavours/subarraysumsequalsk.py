from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [nums[0]] + len(nums)
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        ans = 0
        seen = {}

        for j in range(len(prefixSum)):
            if prefixSum[j] == k:
                ans += 1

            ans += seen.get(prefixSum[j] - k, 0)
            seen[prefixSum[j]] = seen.get(prefixSum[j], 0) + 1

        return ans


        